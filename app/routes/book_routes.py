from flask import Blueprint, request, Response
from app.models.book import Book
from .route_utilities import validate_model, create_model, get_models_with_filters
from ..db import db

bp = Blueprint("books_bp", __name__, url_prefix="/books")

@bp.post("")
def create_book():
    request_body = request.get_json()
    return create_model(Book, request_body)

@bp.get("")
def get_all_books():
    return get_models_with_filters(Book, request.args)

@bp.get("/<book_id>")
def get_one_book(book_id):
    book = validate_model(Book, book_id)
    return book.to_dict()

@bp.put("/<book_id>")
def update_book(book_id):
    book = validate_model(Book, book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json") # 204 No Content

@bp.delete("/<book_id>")
def delete_book(book_id):
    book = validate_model(Book, book_id)
    db.session.delete(book)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


# @bp.get("")
# def get_all_books():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description" : book.description
#             }
#         )
#     return books_response

# @bp.get("/<book_id>")#has a route paramenter so needs to have a function parameter
# def get_one_book(book_id):#this function is called whenever a HTTP request matches ites route decorator
#     book = validate_book(cls, book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }

# def validate_book(cls, book_id):
#     try:
#         book_id = int(book_id)
#     except ValueError:
#         response = {"message": f"book {book_id} invalid"}
#         abort(make_response(response,400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     response = {"message": f"book{book_id} not found"}
#     abort(make_response(response, 404))

# def get_all_books():
# query = db.select(Book).order_by(Book.id)
# books = db.session.scalars(query)
# We could also write the line above as:
# books = db.session.execute(query).scalars()

# books_response = []
# for book in books:
#     books_response.append(
#         {
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         }
#     )
# return books_response
