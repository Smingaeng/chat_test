  "User": {
    "id": "INT",
    "username": "String(50)",
    "email": "String(100)",
    "phone_number": "String(20)",
    "gender": "Enum('남성', '여성')",
    "school": "Enum('중학교', '고등학교')",
    "password": "String(255)"
  },
  "Scenario": {
    "scenario_id": "INT",
    "category_id": "INT",
    "scenario_name": "String(255)",
    "scenario_description": "Text",
    "creation_date": "Date"
  },
  "Category": {
    "category_id": "INT",
    "category_name": "String(255)"
  },
  "ChatMessage": {
    "message_id": "INT",
    "user_id": "INT",
    "chatroom_id": "INT",
    "message_content": "Text",
    "creation_date": "DateTime"
  },
  "Chatroom": {
    "chatroom_id": "INT",
    "scenario_id": "INT",
    "user_id": "INT",
    "chatroom_name": "String(255)",
    "status": "String(50)",
    "creation_date": "DateTime"
  },
  "Mbti": {
    "person_id": "INT",
    "id": "INT",
    "personality_name": "String(255)",
    "personality_description": "Text"
  },
  "MemberServiceLogs": {
    "service_id": "INT",
    "user_id": "INT",
    "signup_date": "Date",
    "password_change_date": "Date",
    "last_login_date": "DateTime",
    "login_count": "INT"
  },
  "Notification": {
    "notification_id": "INT",
    "user_id": "INT",
    "notification_content": "Text",
    "created_at": "DateTime"
  },
  "Quest": {
    "quest_id": "INT",
    "scenario_id": "INT",
    "quest_name": "String(255)",
    "quest_content": "Text"
  },
  "Role": {
    "role_id": "INT",
    "scenario_id": "INT",
    "role_name": "String(255)",
    "role_description": "Text"
  },
  "TermsAndCondition": {
    "terms_id": "INT",
    "agreement_status": "INT",
    "order_number": "INT",
    "content": "Text",
    "title": "String(255)",
    "registration_datetime": "DateTime",
    "registrant": "String(255)"
  },
  "Tip": {
    "tip_id": "INT",
    "scenario_id": "INT",
    "message_id": "INT",
    "tip_content": "Text"
  },
  "TodayConversation": {
    "conversation_id": "INT",
    "user_id": "INT",
    "scenario_id": "INT"
  }
}
