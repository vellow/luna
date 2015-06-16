from app.config.settings import db
from tornado import gen
from tornado.web import HTTPError
import datetime

@gen.coroutine
def find_all(**kwargs):
    try:
        cursor = db.lines.find()
        result = yield cursor.to_list(length=100)
        if result:
            return {
                'success': True,
                'error': None,
                'message': 'ok',
                'data': result
            }
        else:
            return {
                'success': False,
                'error': None,
                'message': 'Not Matched',
                'data': result
            }

    except:
        return {
            'success': False,
            'error': HTTPError(500, log_message='Unkown Server Error')
        }



@gen.coroutine
def save(records, **kwargs):
    try:
        records['last_updated'] = datetime.datetime.now()
        result = yield db.lines.save(records)
        return {
            'success': True,
            'error': None,
            'data': result
        }
    except:
        return {
            'success': False,
            'error': HTTPError(500, log_message='Internal Server Error')
        }


@gen.coroutine
def remove(condition, **kwargs):
    try:
        result = yield db.lines.remove(condition)
        return {
            'success': True,
            'error': None,
            'data': result
        }
    except:
        return {
            'success': False,
            'error': HTTPError(500, log_message='Internal Server Error')
        }

@gen.coroutine
def find_one(condition):
    try:
        result = yield db.lines.find_one(condition)
        if result:
            return {
                'success': True,
                'error': None,
                'message': 'ok',
                'data': result
            }
        else:
            return {
                'success': False,
                'error': None,
                'message': 'Not Matched',
                'data': result
            }

    except:
        return {
            'success': False,
            'error': HTTPError(500, log_message='Unkown Server Error')
        }