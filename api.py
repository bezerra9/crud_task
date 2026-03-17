from fastapi import FastAPI, HTTPException
from schemas.task import TaskCreate, TaskUpdate, Task
from app.config.database import tasks_collection

app = FastAPI(title='API de tasks')


@app.post('/tasks')
async def create_task(nova_task: TaskCreate):
    task_completa  = Task(**nova_task.model_dump())
    task_dict = task_completa.model_dump()

    task_dict['_id'] = task_dict.pop('id') 
    await tasks_collection.insert_one(task_dict)

    return {"message": "Task created succesfuly", "task": task_completa}


@app.get('/tasks')
async def list_task():
    cursor = tasks_collection.find()
    database_task = await cursor.to_list(length=100)

    formated_task = []

    for task in database_task:
        task['id'] = task.pop('_id')
        formated_task.append(task)
    
    return formated_task


@app.get('/tasks/{task_id}')
async def get_task(task_id: str):
    task = await tasks_collection.find_one({'_id': task_id})

    if task:
        task['id'] = task.pop('_id')
        return task
    
    raise HTTPException(status_code=404, detail="Error: Task not found!")


@app.patch('/tasks/{task_id}')
async def update_task(task_id: str, task_atualizada: TaskUpdate):
    dados_atualizados = task_atualizada.model_dump(exclude_unset=True)

    if not dados_atualizados:
        raise HTTPException(status_code=400, detail="Nenhum dado enviado para atualização.")
    resultado = await tasks_collection.update_one(
        {'_id': task_id},
        {'$set': dados_atualizados}
    )
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Erro: Task não encontrada para atualizar!")
        
    task_banco = await tasks_collection.find_one({"_id": task_id})
    task_banco["id"] = task_banco.pop("_id") 
    
    return {"message": "Task updated succesfully!", "task": task_banco}


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: str):
    resultado = await tasks_collection.delete_one({'_id': task_id})

    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Erro: Task não encontrada para deletar!")
        

    return {"message": "Task deleted successfully!"}
