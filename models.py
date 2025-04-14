from sqlmodel import Field, Session, SQLModel, create_engine, select


class NoteBase(SQLModel):
    title: str = Field(index=True)
    content: str


class Note(NoteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    date: str


class NotePublic(NoteBase):
    id: int
    date: str


class NoteCreate(NoteBase):
    title: str
    content: str


class NoteUpdate(SQLModel):
    title: str | None = None
    content: str | None = None

