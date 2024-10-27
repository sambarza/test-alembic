import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mssql+aioodbc://sa:m4zsWP93GWvBrTU@localhost/master?driver=ODBC+Driver+17+for+SQL+Server"

# Set up SQLAlchemy engine for asynchronous operations
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

from models import User

# Insert function to add data asynchronously
async def insert_user(name: str, email: str, session):
    
    new_user = User(name=name, email=email)
    session.add(new_user)
    print(f"Inserted user: {name}, {email}")

async def main():

    inserts = []

    async with SessionLocal() as session:

        async with session.begin():
             
            for i in range(10000):
                inserts.append(insert_user("Sam", f"sam.{i}@example.com", session=session))

        try:
            await asyncio.gather(*inserts)
            await session.commit()
        finally:
            await engine.dispose()

# Run the main function with asyncio
if __name__ == "__main__":
    asyncio.run(main())