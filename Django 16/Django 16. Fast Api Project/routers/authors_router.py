from tkinter.font import names
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from starlette import status

from deps import require_roles, get_db
from helpers import paginate
from schemas import AuthorOut, AuthorCreate
from models import Author, Role

router = APIRouter(prefix="/api/authors", tags=["authors"])

@router.post("/", response_model=AuthorOut, dependencies=[Depends(require_roles(Role.admin))], status_code=201)
def create_author(payload:AuthorCreate, db:Session=Depends(get_db)):
    if db.query(Author).filter_by(name=payload.name).first() is not None:
        raise HTTPException(status_code=400, detail="Author already exists")
    author = Author(name=payload.name.strip())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


@router.get("/", response_model=dict, status_code=200)
def list_authors(
        q:Optional[str] = Query(None),
        order:str = Query("name"),
        page:int = Query(1, ge=1),
        size:int = Query(10, ge=1, le=100),
        db:Session=Depends(get_db)):
    query = db.query(Author)
    if q:
        query = query.filter(Author.name.icontains(q.lower()))
    if order.lstrip("-") not in {"name", "id"}:
        order = "name"
    col = getattr(Author, order.lstrip("-"))
    if order.startswith("-"):
        col = col.desc
    query = query.order_by(col)
    data = paginate(query, page = page, size=size)
    data["results"] = [AuthorOut.from_orm(a) for a in data["results"]]
    return data

@router.patch("/{author_id}", response_model=AuthorOut,dependencies=[Depends(require_roles(Role.admin))], status_code=200)
def update_author(author_id: int, payload:AuthorOut, db:Session=Depends(get_db)):
    author = db.query(Author).get(author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    author.name = payload.name.strip()
    db.commit()
    db.refresh(author)
    return AuthorOut.from_orm(author)


@router.delete("/{author_id}",dependencies=[Depends(require_roles(Role.admin))], status_code=204)
def delete_author(author_id: int, db:Session=Depends(get_db)):
    author = db.query(Author).get(author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(author)
    db.commit()
    return None

