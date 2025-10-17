from typing import Optional, List

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Index,
insert, select, update, delete,
ForeignKey,
CheckConstraint,
UniqueConstraint)
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base,
    relationship,
    Session,
    joinedload,
    selectinload)

from enum import Enum
DATABASE_URL = "sqlite:///test.db"
engine = create_engine(DATABASE_URL)

metadata = MetaData()

core_users = Table(
    "core_users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("email", String(50), nullable=False, unique=True),
    Index("idx_core_users_name", "name"),
)

metadata.create_all(bind=engine, tables=[core_users])

def core_operations():
    # INSERT
    # with engine.begin() as connection:
    #     connection.execute(
    #         insert(core_users),
    #         [
    #             {"name": "Rashid", "email": "rashid@gmail.com"},
    #             {"name": "Rashida", "email": "rashida@gmail.com"},
    #             {"name": "Rashadet", "email": "rashadet@gmail.com"},
    #             {"name": "Rashad", "email": "rashad@gmail.com"},
    #             {"name": "Roshka", "email": "roshka_kroshka@gmail.com"}
    #         ]
    #     )

    # SELECT
    # with engine.connect() as connection:
    #     rows = connection.execute(select(core_users)).fetchall()
    #     for id, name, mail in rows:
    #         print(f"{id}. Name: {name}, Email: {mail}")

    # UPDATE
    # with engine.begin() as connection:
    #     connection.execute(update(core_users)
    #                        .where(core_users.c.name == "Rashid")
    #                        .values(name="Rəşid")
    #                        )
    # with (engine.connect() as connection):
    #     rows = connection.execute(select(core_users, core_users.c.name)
    #                               .where(core_users.c.name.like("%ash%"))
    #                               .order_by(core_users.c.id.desc())
    #                               ).fetchall()
    #     for id, name, mail, n in rows:
    #         print(f"{id}. Name: {name}, Email: {mail}")

    # DELETE
    with engine.begin() as connection:
        connection.execute(delete(core_users).where(core_users.c.name == "Rashida"))


# core_operations()

Base = declarative_base()

class Role(Enum):
    admin = "admin"
    user = "user"

# Many to Many

book_tags = Table(
    "book_tags",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True)
)

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    books = relationship(
        "Book",
        back_populates="author",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    def __repr__(self):
        return f"<Author id = {self.id} name={self.name}>"


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, index=True)
    pages = Column(Integer, nullable=False, default=1)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"), nullable=False)

    author = relationship("Author", back_populates="books")
    tags = relationship("Tag", secondary= book_tags, back_populates="books")

    __table_args__ = (
        CheckConstraint("pages >= 1", 'ck_books_pages_ge_1'),
        UniqueConstraint("title", "author_id", name="uq_book_title_author")
    )

    def __repr__(self):
        return f"<Book id = {self.id} title={self.title} pages={self.pages}>"


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    books = relationship("Book", back_populates="tags", secondary= book_tags)

    def __repr__(self):
        return f"<Tag id = {self.id} name={self.name}"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    role = Column(String(20), nullable=False, default=Role.user.value)

    def __repr__(self):
        return f"<User id = {self.id} email={self.email} role={self.role}"

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_author(db: Session, name: str)->Author:
    author = Author(name=name)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


def create_book(db: Session, title: str, pages: int, author_id:int,
                tags: Optional[List[str]] = None) -> Book:
    if pages <= 0:
        raise ValueError("pages must be a positive integer")
    book = Book(title=title, pages=pages, author_id=author_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def list_books(db: Session, search:Optional[str] = None,
               limit: int=50, offset: int = 0) -> List[Book]:
    books = select(Book).order_by(Book.id)
    if search:
        books = books.where(Book.title.ilike(f"%{search}%"))
    books = books.offset(offset).limit(limit)
    books = books.options(selectinload(Book.author), selectinload(Book.tags))
    return list(db.execute(books).scalars())


def get_book(db: Session, book_id: int) -> Optional[Book]:
    book = (select(Book).where(Book.id == book_id)
            .options(joinedload(Book.author), selectinload(Book.tags))
            )
    return db.execute(book).scalar_one_or_none()

def delete_book(db: Session, book_id: int)->bool:
    book = db.get(Book, book_id)
    if not book:
        return False
    db.delete(book)
    db.commit()
    return True


def update_book(db: Session, book_id: int, title: Optional[str] = None, pages: Optional[int] = None)->Optional[Book]:
    book = db.get(Book, book_id)
    if not book:
        return None
    if title is not None:
        book.title = title
    if pages is not None:
        if pages < 1:
            raise ValueError("pages must be a positive integer")
        book.pages = pages
    db.commit()
    db.refresh(book)
    return book



db = SessionLocal()
# author1 = create_author(db, name="George Orwell")
# author2 = create_author(db, name="Daniel Keyes")
#
# book1 = create_book(db, title="Animal Farm", pages=92,
#                     author_id=author1.id, tags=["dystopian", "novella"])
#
# book2 = create_book(db, title="1984", pages=328,
#                     author_id=author1.id, tags=["dystopian", "political fiction"])
#
# book3 = create_book(db, title="Flowers for Algernon", pages=311,
#                     author_id=author2.id, tags=["novella"])


# books = list_books(db)
# for book in books:
#     print(book)

# print()
# print(get_book(db, 1).author.name)
# print()
# print(delete_book(db, 2))

update_book(db, 1, pages=110)

