from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user(user_id: Annotated[
    int, Path(gt=0, le=100, description="Enter User ID", example="1", minimum=1, maximum=100)]) -> dict:
    return {"Вы вошли как пользователь №": user_id}


@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[
    str, Path(description="Enter username", example="UrbanUser", min_length=5, max_length=20)],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> dict:
    return {"message": f"Информация о пользователе. Имя: '{username}', Возраст: {age}."}


@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}
