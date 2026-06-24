import datetime
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test_db1 import Base, Student, Subject, Teacher

DATABASE_URL = "sqlite:///mydatabase.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Автоматически создает таблицы перед тестами."""
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session():
    """Для изоляции каждого теста."""
    session = Session()
    yield session
    session.rollback()
    session.close()


def test_add_student(db_session):
    """Тест 1: Добавление студента"""
    new_student = Student(name="Иван Иванов", age=20)
    db_session.add(new_student)
    db_session.commit()

    saved_student = db_session.query(Student).filter_by(
        name="Иван Иванов"
    ).first()
    assert saved_student is not None
    assert saved_student.age == 20


def test_update_subject(db_session):
    """Тест 2: Изменение предмета"""
    new_subject = Subject(title="Базы Данных", hours=40)
    db_session.add(new_subject)
    db_session.commit()

    new_subject.hours = 52
    db_session.commit()

    updated = db_session.query(Subject).filter_by(
        title="Базы Данных"
    ).first()
    assert updated is not None
    assert updated.hours == 52


def test_soft_delete_teacher(db_session):
    """Тест 3: Удаление преподавателя"""
    new_teacher = Teacher(name="Профессор Сидоров")
    db_session.add(new_teacher)
    db_session.commit()

    new_teacher.deleted_at = datetime.datetime.now()
    db_session.commit()

    deleted = db_session.query(Teacher).filter_by(
        name="Профессор Сидоров"
    ).first()
    assert deleted is not None
    assert deleted.deleted_at is not None

    active_teachers = db_session.query(Teacher).filter(
        Teacher.deleted_at.is_(None)
    ).all()
    assert deleted not in active_teachers
