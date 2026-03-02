from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from dotenv import load_dotenv
import os

load_dotenv()

async_engine = create_async_engine(
    url=os.environ("DB_CONNECTION_URI")
)


async def init_db():
    pass


async def get_session():
    session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    ) 
    
    async with session() as async_session:
        yield async_session
        


