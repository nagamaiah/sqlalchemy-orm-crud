from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import sys

# SQLite database connection
engine = create_engine('sqlite:///my_sqlite_database.db', echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# Example User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

# CRUD Operations

def create_user(name: str, email: str):
    session = SessionLocal()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    return user

def get_user(user_id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user

def get_all_users():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return users

def update_user(user_id: int, name: str = None, email: str = None):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        session.commit()
        session.refresh(user)
    session.close()
    return user

def delete_user(user_id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()
    return user

# Example usage (uncomment to test)
# new_user = create_user("lessa", "lessa@example.com")
# print(f"Created user id is {get_user(new_user.id).id}")

# update_user(4, name="Nags", email="test12@gmail.com")

# delete_user(4)

if(len(get_all_users()) > 0):
    for user in get_all_users():  
        print(f"User: id={user.id}, name={user.name}, email={user.email}")
else:
    print("No users found.")   
