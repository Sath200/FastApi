from fastapi import FastAPI

app = FastAPI()

employees = ["Karen", "John"]


@app.get("/employees")
async def get_employees():
    return employees


@app.post("/employees")
async def post_employee(name: str):
    employees.append(name)
    return employees


@app.put("/employees/{name}")
async def put_employee(name: str, new_name: str):
    old = employees.index(name)
    employees[old] = new_name
    return employees


@app.delete("/employees/{name}")
async def del_employee(name: str):
    employees.remove(name)
    return employees
