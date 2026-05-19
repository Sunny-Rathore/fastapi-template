from multiprocessing.managers import DictProxy

from jose import jwt, JWTError

from app.exceptions.app_exception import AppException
SECRET_KEY : str ='my_key'

#crete token
def create_Jwt_token(payload:dict)->str:
    return jwt.encode(
        payload,
        SECRET_KEY,
        )


#verify token
def verify_token(token:str)-> dict:
    try :
      return jwt.decode(token,SECRET_KEY)
    except JWTError :
        raise AppException('invalid token',401)
        