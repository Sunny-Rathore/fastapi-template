from typing import Any

from fastapi.responses import JSONResponse

def successResponse(data:Any,message :str='success',status_code :int=200):
    return JSONResponse(
        status_code=status_code,
        content={
        'success': True,
        'message': message,
        "data": data
    }
    )

def errorResponse(message :str='error',status_code: int=500):
    return JSONResponse(
        status_code=status_code,
        content= {
        "success":False,
        'message':message
    }
    )
