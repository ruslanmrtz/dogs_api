from fastapi import FastAPI, Depends, HTTPException
import datetime
from typing import Dict, List, Type
from sqlalchemy.orm import Session

from config import SessionLocal
from schemas import Dog, DogType, Timestamp
from models import DogDB

app = FastAPI()


def get_session():
    with SessionLocal() as session:
        return session


@app.get('/')
def Root():
    """
    Корневой get-запрос
    """
    return "string"


@app.post('/post', response_model=Timestamp)
def get_post() -> dict[str, int]:
    """
    Обработка POST-Запроса
    """
    result = {
        "id": 0,
        "timestamp": 0
    }

    return result


@app.get('/dogs', response_model=List[Dog])
def get_dogs(kind: DogType, db: Session = Depends(get_session)):

    """
    Получить список собак в Базе Данных
    """

    return db.query(DogDB).filter(DogDB.kind == kind).all()


@app.post('/dogs', response_model=Dog)
def create_dog(dog: Dog, db: Session = Depends(get_session)):

    """
    Запись собаки в Базу Данных
    """

    dog_db = DogDB(name=dog.name, pk=dog.pk, kind=dog.kind)

    db.add(dog_db)

    db.commit()

    db.refresh(dog_db)

    return dog_db


@app.get('/dog/{pk}', response_model=Dog)
def get_dog_by_pk(pk: int, db: Session = Depends(get_session)):

    """
    Получение собаки по ключу
    """

    return db.query(DogDB).filter(DogDB.pk == pk).all()


@app.patch('/dog/{pk}', response_model=Dog)
def update_dog(pk: int, dog: Dog, db: Session = Depends(get_session)):
    """
    Обновление собаки по ключу
    """

    dog_db = db.query(DogDB).filter(DogDB.pk == pk).first()

    if dog_db is None:
        raise HTTPException(status_code=404, detail="Dog not found")

    dog_db.name = dog.name
    dog_db.kind = dog.kind

    db.commit()
    db.refresh(dog_db)

    return dog_db





