import sys
sys.path.append('./')

from connection import db_session
from model.sql_model import Todo
import decoders.todo as decode

# create a todo

def create_to_do(root: str, synonyms: list) -> dict:
    try:
        req = Todo(root=root, synonyms=synonyms)
        db_session.add(req)
        db_session.commit()
        return {
            'status': 'ok',
            'message': 'Created new todo'
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

# synonyms_list = ["mmbl","Mobilink Microfinance Bank Ltd", "Mobilink Microfinance Bank Limited", "Mobilink Microfinance Bank"]
# res = create_to_do(None, synonyms_list)
# print(res)

# get all todo

def get_all():
    try:
        res = db_session.query(Todo).all()
        docs = decode.decode_todos(res)
        return {
            'status': 'ok',
            'data': docs
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }
        
# res = get_all()
# print(res)

# get one todo 

def get_one(id: int):
    try:
        res = db_session.query(Todo).filter_by(id=id).one_or_none()
        if res is not None:
            return {
                'status': 'ok',
                'data': decode.decode_todo(res)
            }
        else:
            return {
                'status': 'error',
                'message': f'Record with id {id} not found.'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

# res = get_one(1)
# print(res)

# update todo

def update_todo(id: int, synonyms: list):
    try:
        criteria = {'id': id}
        todo_item = db_session.query(Todo).filter_by(**criteria).one_or_none()

        if todo_item is not None:
            todo_item.synonyms = synonyms
            db_session.commit()

            return {
                'status': 'ok',
                'message': f'Todo with id {id} updated successfully.'
            }
        else:
            return {
                'status': 'error',
                'message': f'Todo with id {id} not found.'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

# synonyms_list = ["MMBL","Mobilink Microfinance Bank Ltd", "Mobilink Microfinance Bank Limited", "Mobilink Microfinance Bank"]   
# res = update_todo(1, synonyms_list)
# print(res)

#delete todo 

def delete_todo(id: int):
    try:
        criteria = {'id': id}
        todo_item = db_session.query(Todo).filter_by(**criteria).one_or_none()

        if todo_item is not None:
            db_session.delete(todo_item)
            db_session.commit()

            return {
                'status': 'ok',
                'message': f'Todo with id {id} deleted successfully.'
            }
        else:
            return {
                'status': 'error',
                'message': f'Todo with id {id} not found.'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

res = delete_todo(1)
print(res)