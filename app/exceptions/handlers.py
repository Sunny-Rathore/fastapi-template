
from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError
from typing import cast

from app.exceptions.app_exception import AppException
from app.utils.response_utils import errorResponse

# Validation Exception handler
async def validation_exception_handler(
    request: Request,
    exc: Exception
):
  validation_exc = cast(RequestValidationError, exc)
  field = validation_exc.errors()[0]['loc'][1]
  message = validation_exc.errors()[0]['msg']
  return errorResponse(f"{field} {message}",422)


# HTTP exception handler
async def http_exception_handler(
    request: Request,
    exc: Exception
):
    http_exception = cast(HTTPException ,exc)
    return errorResponse(http_exception.detail,http_exception.status_code)


# Global error handler      
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    return errorResponse("Internal Server Error",500)


# App exception handler
async def app_exception_handler(
    request : Request,
    exc : Exception
):
   app_exception = cast(AppException ,exc)
   return errorResponse(app_exception.message,app_exception.status_code)