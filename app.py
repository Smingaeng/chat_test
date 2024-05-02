from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel
from database import engineconn
from models import User
from models import Test

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()

class Item(BaseModel):
    name: str
    number: int

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    phone_number: str
    gender: str
    school: str

# 모든 사용자 정보를 반환하는 엔드포인트
@app.get("/users")
async def read_users():
    users = session.query(User).all()
    return users

# 특정 id로 사용자 정보 조회
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        return {"message": "User not found"}
    return user.dict()

# 사용자 관련 API
@app.post("/create_user/")
async def create_user(item: Item):
    new_user = Test(name=item.name, number=item.number)
    session.add(new_user)
    session.commit()
    return {"message": "User created successfully"}

# @app.get("/get_user/{user_id}")
# async def get_user(user_id: int):
#     user = session.query(Test).filter(Test.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

@app.put("/update_user/{user_id}")
async def update_user(user_id: int, item: Item):
    user = session.query(Test).filter(Test.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = item.name
    user.number = item.number
    session.commit()
    return {"message": "User updated successfully"}

@app.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    user = session.query(Test).filter(Test.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": "User deleted successfully"}