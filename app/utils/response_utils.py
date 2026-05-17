from fastapi.responses import JSONResponse

def successResponse(data,message='success',status_code=200):
    return JSONResponse(
        status_code=status_code,
        content={
        'success': True,
        'message': message,
        "data": data
    }
    )



def errorResponse(message='error',status_code=500):
    return JSONResponse(
        status_code=status_code,
        content= {
        "success":False,
        'message':message
    }
    )
