from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4
from datetime import datetime


class User(SQLModel, table=True):   
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(unique=True)
    password: str | None = Field(default=None, nullable=True)
    username: str | None = Field(nullable=False)
    joined_at: datetime = Field(default_factory=datetime.now)
    
    zweets: list["Zweet"] = Relationship(back_populates="user", cascade_delete=True)
    
    
class Zweet(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    content: str = Field()
    posted_at: datetime = Field(default_factory=datetime.now)
    user_id: UUID = Field(foreign_key="user.id", ondelete="CASCADE")
    
    user: User = Relationship(back_populates="zweets")