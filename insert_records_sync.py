from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User

def insert_users(engine):
    session = Session(bind=engine)
    
    try:

        for i in range(10000):
            user = User(name="Alice", email=f"sam.{i}@example.com")
            session.add(user)
            print(f"Inserted {f"sam.{i}@example.com"}")

        session.commit()

        print("Record inseriti con successo!")
    except Exception as e:
        session.rollback()
        print(f"Errore durante l'inserimento dei record: {e}")
    finally:
        session.close()

if __name__ == "__main__":

    DATABASE_URL = "mssql+pyodbc://sa:m4zsWP93GWvBrTU@localhost/master?driver=ODBC+Driver+17+for+SQL+Server"
    engine = create_engine(DATABASE_URL)

    insert_users(engine)
