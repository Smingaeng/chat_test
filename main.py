from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel
from database import engineconn
from models import User

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

    user_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "phone_number": user.phone_number,
        "gender": user.gender,
        "school": user.school,
        "password": user.password
    }

    return user_data
# 사용자 등록
@app.post("/users/")
async def create_user(item: Item):
    user = User(**item.dict())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
# 특정 사용자 정보 업데이트
@app.put("/users/{user_id}")
async def update_user(user_id: int, item: Item):
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in item.dict().items():
        setattr(user, key, value)
    session.commit()
    session.refresh(user)
    return user

# 특정 사용자 삭제
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": "User deleted successfully"}

# # 모든 시나리오 조회
# @app.get("/scenarios")
# async def read_scenarios():
#     scenarios = session.query(Scenario).all()
#     return scenarios
#
# # 새 시나리오 생성
# @app.post("/scenarios/")
# async def create_scenario(item: Item):
#     scenario = Scenario(**item.dict())
#     session.add(scenario)
#     session.commit()
#     session.refresh(scenario)
#     return scenario
#
# # 특정 시나리오 조회
# @app.get("/scenarios/{scenario_id}")
# async def read_scenario(scenario_id: int):
#     scenario = session.query(Scenario).filter(Scenario.id == scenario_id).first()
#     if scenario is None:
#         raise HTTPException(status_code=404, detail="Scenario not found")
#     return scenario
#
# # 특정 시나리오 삭제
# @app.delete("/scenarios/{scenario_id}")
# async def delete_scenario(scenario_id: int):
#     scenario = session.query(Scenario).filter(Scenario.id == scenario_id).first()
#     if scenario is None:
#         raise HTTPException(status_code=404, detail="Scenario not found")
#     session.delete(scenario)
#     session.commit()
#     return {"message": "Scenario deleted successfully"}
#
# # 모든 피드백 조회
# @app.get("/feedbacks")
# async def read_feedbacks():
#     feedbacks = session.query(Feedback).all()
#     return feedbacks
#
# # 새 피드백 생성
# @app.post("/feedbacks/")
# async def create_feedback(item: Item):
#     feedback = Feedback(**item.dict())
#     session.add(feedback)
#     session.commit()
#     session.refresh(feedback)
#     return feedback
#
# # 특정 피드백 조회
# @app.get("/feedbacks/{feedback_id}")
# async def read_feedback(feedback_id: int):
#     feedback = session.query(Feedback).filter(Feedback.id == feedback_id).first()
#     if feedback is None:
#         raise HTTPException(status_code=404, detail="Feedback not found")
#     return feedback
#
# # 특정 피드백 삭제
# @app.delete("/feedbacks/{feedback_id}")
# async def delete_feedback(feedback_id: int):
#     feedback = session.query(Feedback).filter(Feedback.id == feedback_id).first()
#     if feedback is None:
#         raise HTTPException(status_code=404, detail="Feedback not found")
#     session.delete(feedback)
#     session.commit()
#     return {"message": "Feedback deleted successfully"}
#
# # 모든 역할 조회
# @app.get("/roles")
# async def read_roles():
#     roles = session.query(Role).all()
#     return roles
#
# # 새 역할 생성
# @app.post("/roles/")
# async def create_role(item: Item):
#     role = Role(**item.dict())
#     session.add(role)
#     session.commit()
#     session.refresh(role)
#     return role
#
# # 특정 역할 정보 업데이트
# @app.put("/roles/{role_id}")
# async def update_role(role_id: int, item: Item):
#     role = session.query(Role).filter(Role.id == role_id).first()
#     if role is None:
#         raise HTTPException(status_code=404, detail="Role not found")
#     for key, value in item.dict().items():
#         setattr(role, key, value)
#     session.commit()
#     session.refresh(role)
#     return role
#
# # 특정 역할 삭제
# @app.delete("/roles/{role_id}")
# async def delete_role(role_id: int):
#     role = session.query(Role).filter(Role.id == role_id).first()
#     if role is None:
#         raise HTTPException(status_code=404, detail="Role not found")
#     session.delete(role)
#     session.commit()
#     return {"message": "Role deleted successfully"}