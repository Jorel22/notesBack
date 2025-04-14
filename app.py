from fastapi import FastAPI, Depends, Query, HTTPException
from typing import Annotated
from models import Note, NoteCreate, NotePublic, NoteUpdate
from sqlmodel import Session, SQLModel, create_engine, select
from contextlib import asynccontextmanager

sqlite_file_name = "notes1.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    pass


app = FastAPI(debug=True, lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/notes", response_model=NotePublic)
def create_note(note: NoteCreate, session: SessionDep) -> Note:
    db_note = Note.model_validate(note)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return note


@app.get("/notes", response_model=list[NotePublic])
def get_notes(
    session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100
) -> list[Note]:
    notes = session.exec(select(Note).offset(offset).limit(limit)).all()
    return notes


@app.get("/notes/{note_id}", response_model=NotePublic)
def get_note(note_id: int, session: SessionDep) -> Note:
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.delete("/notes/{note_id}")
def delete_note(note_id: int, session: SessionDep) -> dict:
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    session.delete(note)
    session.commit()
    return {"ok": True}


@app.put("/notes/{note_id}", response_model=NotePublic)
def update_note(note_id: int, note: NoteUpdate, session: SessionDep):
    db_note = session.get(Note, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    note_data = Note.model_dump(exclude_unset=True)
    db_note.sqlmodel_update(note_data)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note
