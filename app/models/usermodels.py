from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config.database import Base


class User(Base):
    __tablename__ = "users"  

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    mobile = Column(String)
    is_active = Column(Boolean, default=True)

    #reviews = relationship("ReviewModel", back_populates="user")

    def __repr__(self):
        return f"<User {self.email}"
