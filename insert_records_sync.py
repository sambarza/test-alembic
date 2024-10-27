from sqlalchemy.orm import Session
from models import User, engine

def insert_users():
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
    insert_users()
