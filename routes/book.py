from fastapi import APIRouter, Response
from config.db import conn
from schemas.book import bookEntity,booksEntity
from models.book import Book
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


book = APIRouter()

@book.get('/book',tags=["books"])
def find_all_book():
    return booksEntity(conn.mintic.book.find())   

@book.post('/book',tags=["books"])
def create_book(book:Book):
    new_book = dict(book) 
    del new_book["id"] 

    
    id = conn.mintic.book.insert_one(new_book).inserted_id
    book = conn.mintic.book.find_one({"_id":id}) 
    return bookEntity(book)  

@book.get('/book/{id}',tags=["books"])
def find_user(id:str):
    return bookEntity(conn.mintic.book.find_one({"_id":ObjectId(id)})) 

@book.put('/book/{id}',tags=["books"])
def update_book(id:str,book:Book):
    conn.mintic.book.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(book)})
    return bookEntity(conn.mintic.book.find_one({"_id":ObjectId(id)}))  

@book.delete('/book/{id}',tags=["books"])
def delete_book(id:str):
    bookEntity(conn.mintic.book.find_one_and_delete({"_id":ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT) 

