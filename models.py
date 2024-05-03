from sqlalchemy import Column, TEXT, INT, BIGINT, Integer, String, Enum, Date, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Test(Base):
    __tablename__ = "test"

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(TEXT, nullable=False)
    number = Column(INT, nullable=False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    phone_number = Column(String(20))
    gender = Column(Enum('남성', '여성'))
    school = Column(Enum('중학교', '고등학교'))
    password = Column(String(255))

    # 다른 클래스와의 관계 설정
    mbti = relationship("Mbti", back_populates="user")
    memberServiceLogs = relationship("MemberServiceLogs", back_populates="user")
    notifications = relationship("Notification", back_populates="user")
    today_conversations = relationship("TodayConversation", back_populates="user")


class Scenario(Base):
    __tablename__ = 'scenarios'

    scenario_id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    scenario_name = Column(String(255))
    scenario_description = Column(Text)
    creation_date = Column(Date)

    # 다른 클래스와의 관계 설정
    category = relationship("Category")
    chatrooms = relationship("Chatroom", back_populates="scenario")
    quests = relationship("Quest", back_populates="scenario")
    roles = relationship("Role", back_populates="scenario")
    tips = relationship("Tip", back_populates="scenario")
    today_conversations = relationship("TodayConversation", back_populates="scenario")

class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(255))

    # 다른 클래스와의 관계 설정
    scenario = relationship("Scenario", back_populates="chatrooms")
    user = relationship("User", back_populates="chatrooms")

class ChatMessage(Base):
    __tablename__ = 'chat_messages'

    message_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    chatroom_id = Column(Integer, ForeignKey('Chatroom.chatroom_id'))
    message_content = Column(Text)
    creation_date = Column(DateTime, default=datetime.now)

    # User와의 관계 설정
    user = relationship("User")

    # Chatroom과의 관계 설정
    chatroom = relationship("Chatroom")


class Chatroom(Base):
    __tablename__ = 'chatrooms'

    chatroom_id = Column(Integer, primary_key=True, index=True)
    scenario_id = Column(Integer, ForeignKey('Scenario.id'))
    user_id = Column(Integer, ForeignKey('User.id'))
    chatroom_name = Column(String(255))
    status = Column(String(50))
    creation_date = Column(DateTime, default=datetime.now)

    # Scenario와의 관계 설정
    scenario = relationship("Scenario")

    # User와의 관계 설정
    user = relationship("User")

class Mbti(Base):
    __tablename__ = 'mbti'

    person_id = Column(Integer, primary_key=True, index=True)
    id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    personality_name = Column(String(255))
    personality_description = Column(Text)

    # User와의 관계 설정
    user = relationship("User", back_populates="mbti")

class MemberServiceLogs(Base):
    __tablename__ = 'member_service_logs'

    service_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    signup_date = Column(Date)
    password_change_date = Column(Date)
    last_login_date = Column(DateTime)
    login_count = Column(Integer)

    user = relationship("User", back_populates="memberServiceLogs")

class Notification(Base):
    __tablename__ = 'notifications'

    notification_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    notification_content = Column(Text)
    created_at = Column(DateTime)

    user = relationship("User", back_populates="notifications")

class Quest(Base):
    __tablename__ = 'quests'

    quest_id = Column(Integer, primary_key=True)
    scenario_id = Column(Integer, ForeignKey('Scenario.scenario_id'), primary_key=True)
    quest_name = Column(String(255))
    quest_content = Column(Text)

    scenario = relationship("Scenario", back_populates="quests")

class Role(Base):
    __tablename__ = 'roles'

    role_id = Column(Integer, primary_key=True)
    scenario_id = Column(Integer, ForeignKey('Scenario.scenario_id'), primary_key=True)
    role_name = Column(String(255))
    role_description = Column(Text)

    scenario = relationship("Scenario", back_populates="roles")

class TermsAndCondition(Base):
    __tablename__ = 'terms_and_conditions'

    terms_id = Column(Integer, primary_key=True)
    agreement_status = Column(Integer)
    order_number = Column(Integer)
    content = Column(Text)
    title = Column(String(255))
    registration_datetime = Column(DateTime)
    registrant = Column(String(255))

class Tip(Base):
    __tablename__ = 'tips'

    tip_id = Column(Integer, primary_key=True)
    scenario_id = Column(Integer,  ForeignKey('Scenario.scenario_id'), primary_key=True)
    message_id = Column(Integer, ForeignKey('chat_messages.message_id'))
    tip_content = Column(Text)

    # 'scenarios' 테이블과의 관계 설정
    scenario = relationship("Scenario", back_populates="tips")

    # 'chat_messages' 테이블과의 관계 설정
    chat_message = relationship("ChatMessage")

class TodayConversation(Base):
    __tablename__ = 'today_conversations'

    conversation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    scenario_id = Column(Integer, ForeignKey('scenarios.scenario_id'))

    # 'users' 테이블과의 관계 설정
    user = relationship("User", back_populates="today_conversations")

    # 'scenarios' 테이블과의 관계 설정
    scenario = relationship("Scenario")