from pydoc import cli

from fastapi import FastAPI
from app.exceptions.app_exception import AppException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError,HTTPException

from app.core.database import client
from app.modules.user.user_routes import router as user_router
from app.modules.auth.auth_routes import router as auth_router
from app.exceptions.handlers import (
http_exception_handler,
validation_exception_handler,
global_exception_handler,
app_exception_handler,
)

app = FastAPI()
@app.on_event('startup')
async def startup():
    print('server started')
    try:
        await client.admin.command('ping')
        print("MongoDB connected successfully")
    except Exception as e :
        print(f"MongoDB connection failed: {e}")
            

origins = [
    "http://localhost:3000",
    "https://yourfrontend.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials= True,
    allow_methods =["*"],
    allow_headers =["*"]         
                   )

app.include_router(user_router)
app.include_router(auth_router)

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
def root():
    return {
        'message':"Api is running"
    }
