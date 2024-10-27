from sqlalchemy.orm import Session
from models import User, engine

def insert_users():
    session = Session(bind=engine)
    
    try:
        user1 = User(name="Alice", email="alice@example.com")
        user2 = User(name="Bob", email="bob@example.com")
        
        session.add(user1)
        session.add(user2)
        
        session.commit()

        print("Record inseriti con successo!")
    except Exception as e:
        session.rollback()
        print(f"Errore durante l'inserimento dei record: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    insert_users()
