from fastapi import FastAPI
from app.exceptions.app_exception import AppException
from app.modules.user.user_routes import router as user_router
from fastapi.exceptions import RequestValidationError,HTTPException
from app.exceptions.handlers import http_exception_handler ,validation_exception_handler ,global_exception_handler,app_exception_handler

app = FastAPI()
app.include_router(user_router)


app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    AppException,
    app_exception_handler)

app.add_exception_handler(
    Exception,
    global_exception_handler
)
 
@app.get('/')
def home():
    return {
        'message':"Api is running"
    }
