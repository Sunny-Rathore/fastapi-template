from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError
from app.exceptions.app_exception import AppException
from app.utils.response_utils import errorResponse

async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
  field = exc.errors()[0]['loc'][1]
  message = exc.errors()[0]['msg']
  return errorResponse(f"{field} {message}",422)

async def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return errorResponse(exc.detail,exc.status_code)
     
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    return errorResponse("Internal Server Error",500)

async def app_exception_handler(
      request:Request,
      exc =AppException
):
   return errorResponse(exc.message,exc.status_code)