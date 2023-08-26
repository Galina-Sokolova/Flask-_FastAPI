# Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок
# и описание. Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
# Для этого использовать библиотеку Pydantic.
import enum
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Status(enum.Enum):
    todo = 'todo'
    in_progress = 'in progress'
    done = 'done'


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: Status


class TaskInput(BaseModel):
    title: str
    description: str
    status: Status


tasks = []

app = FastAPI()


@app.get("/tasks/", response_model=list[Task])
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task


@app.post("/tasks/", response_model=list[Task])
def new_task(task: TaskInput):
    task = Task(
        id=len(tasks) + 1,
        title=task.title,
        description=task.description,
        status=task.status
    )
    tasks.append(task)
    return tasks


@app.put("/tasks/{task_id}", response_model=TaskInput)
def edit_task(task_id: int, new_task: Task):
    for task in tasks:
        if task.id == task_id:
            task.title = new_task.title
            task.description = new_task.description
            task.status = new_task.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", response_model=str)
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return "task was deleted"
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
