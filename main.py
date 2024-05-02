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

# # 시나리오 관련 모델
# class Scenario(BaseModel):
#     id: int
#     name: str
#
# # 피드백 관련 모델
# class Feedback(BaseModel):
#     id: int
#     text: str
#
# # 역할 관련 모델
# class Role(BaseModel):
#     id: int
#     name: str
#
# # 사용자 관련 API
# @app.get("/users", response_model=List[User])
# async def read_users():
#     return users
#
# @app.post("/users", response_model=User)
# async def create_user(user: User):
#     users.append(user)
#     return user
#
# @app.get("/users/{user_id}", response_model=User)
# async def read_user(user_id: int):
#     for user in users:
#         if user.id == user_id:
#             return user
#     raise HTTPException(status_code=404, detail="User not found")
#
# @app.put("/users/{user_id}", response_model=User)
# async def update_user(user_id: int, user: User):
#     for i, u in enumerate(users):
#         if u.id == user_id:
#             users[i] = user
#             return user
#     raise HTTPException(status_code=404, detail="User not found")
#
# @app.delete("/users/{user_id}")
# async def delete_user(user_id: int):
#     for i, user in enumerate(users):
#         if user.id == user_id:
#             del users[i]
#             return {"message": "User deleted successfully"}
#     raise HTTPException(status_code=404, detail="User not found")
#
# # 시나리오 관련 API
# @app.get("/scenarios", response_model=List[Scenario])
# async def read_scenarios():
#     return scenarios
#
# @app.post("/scenarios", response_model=Scenario)
# async def create_scenario(scenario: Scenario):
#     scenarios.append(scenario)
#     return scenario
#
# @app.get("/scenarios/{scenario_id}", response_model=Scenario)
# async def read_scenario(scenario_id: int):
#     for scenario in scenarios:
#         if scenario.id == scenario_id:
#             return scenario
#     raise HTTPException(status_code=404, detail="Scenario not found")
#
# @app.delete("/scenarios/{scenario_id}")
# async def delete_scenario(scenario_id: int):
#     for i, scenario in enumerate(scenarios):
#         if scenario.id == scenario_id:
#             del scenarios[i]
#             return {"message": "Scenario deleted successfully"}
#     raise HTTPException(status_code=404, detail="Scenario not found")
#
# # 피드백 관련 API
# @app.get("/feedbacks", response_model=List[Feedback])
# async def read_feedbacks():
#     return feedbacks
#
# @app.post("/feedbacks", response_model=Feedback)
# async def create_feedback(feedback: Feedback):
#     feedbacks.append(feedback)
#     return feedback
#
# @app.get("/feedbacks/{feedback_id}", response_model=Feedback)
# async def read_feedback(feedback_id: int):
#     for feedback in feedbacks:
#         if feedback.id == feedback_id:
#             return feedback
#     raise HTTPException(status_code=404, detail="Feedback not found")
#
# @app.delete("/feedbacks/{feedback_id}")
# async def delete_feedback(feedback_id: int):
#     for i, feedback in enumerate(feedbacks):
#         if feedback.id == feedback_id:
#             del feedbacks[i]
#             return {"message": "Feedback deleted successfully"}
#     raise HTTPException(status_code=404, detail="Feedback not found")
#
# # 역할 관련 API
# @app.get("/roles", response_model=List[Role])
# async def read_roles():
#     return roles
#
# @app.post("/roles", response_model=Role)
# async def create_role(role: Role):
#     roles.append(role)
#     return role
#
# @app.put("/roles/{role_id}", response_model=Role)
# async def update_role(role_id: int, role: Role):
#     for i, r in enumerate(roles):
#         if r.id == role_id:
#             roles[i] = role
#             return role
#     raise HTTPException(status_code=404, detail="Role not found")
#
# @app.delete("/roles/{role_id}")
# async def delete_role(role_id: int):
#     for i, role in enumerate(roles):
#         if role.id == role_id:
#             del roles[i]
#             return {"message": "Role deleted successfully"}
#     raise HTTPException(status_code=404, detail="Role not found")
