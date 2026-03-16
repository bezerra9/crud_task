from fastapi import FastAPI, HTTPException
from schemas.task import TaskCreate, TaskUpdate, Task

bd_improvisado = []

app = FastAPI(title='API de tasks')


@app.post('/tasks')
async def create_task(nova_task: TaskCreate):
    task_completa  = Task(**nova_task.model_dump())
    bd_improvisado.append(task_completa.model_dump())
    return {"message": "Task created succesfuly", "task": task_completa}


@app.get('/tasks')
async def list_task():
    return bd_improvisado


@app.get('/tasks/{task_id}')
async def get_task(task_id: str):

    for task in bd_improvisado:
        if task['id'] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Error: Task not found!")


@app.patch('/tasks/{task_id}')
async def update_task(task_id: str, task_atualizada: TaskUpdate):
    
    for task in bd_improvisado:
        if task['id'] == task_id:
            task['status'] = task_atualizada.status
            return {"message": "Task updated succesfully!", "task": task}
        
    raise HTTPException(status_code=404, detail="Erro: Task não encontrada para atualizar!")


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: str):
    
    for task in bd_improvisado:
        if task['id'] == task_id:
            bd_improvisado.remove(task)
            return {"message": "Task deleted successfully!"}
        
    raise HTTPException(status_code=404, detail="Erro: Task não encontrada para deletar!")
