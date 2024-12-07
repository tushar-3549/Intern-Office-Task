from fastapi import APIRouter
from model.pydantic_model import Todo 
import all_routes 
import operations.to_do as db


todo_route = APIRouter()
# post 
@todo_route.post(all_routes.todo_create)
def new_todo(doc: Todo):
    doc = dict(doc)
    # return doc
    root: str = doc['root']
    synonyms: list = doc['synonyms']
    res = db.create_to_do(root, synonyms)
    return res

# get all
@todo_route.get(all_routes.todo_all)
def all_todos():
    res = db.get_all()
    return res

# get one 
@todo_route.get(all_routes.todo_one)
def todo_one(id: int):
    res = db.get_one(id)
    return res

# update one
@todo_route.patch(all_routes.todo_update)
def todo_update(id: int, doc: Todo):
    doc = dict(doc)
    synonyms: list = doc['synonyms']
    res = db.update_todo(id, synonyms)
    return res

# delete one 
@todo_route.delete(all_routes.todo_delete)
def todo_update(id: int):
    res = db.delete_todo(id)
    return res
