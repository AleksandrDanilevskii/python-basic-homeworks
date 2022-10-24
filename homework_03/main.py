from fastapi import FastAPI, status, HTTPException
from fastapi.exception_handlers import http_exception_handler
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/ping/", status_code=status.HTTP_200_OK)
def ping():
    return {"message": "pong"}


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def custom_404_handler(request, exception):
    if (isinstance(exception, HTTPException)
            and exception.detail != "Not Found1"):
        return await http_exception_handler(request, exception)

    return JSONResponse(
        {
            "request url": request.url.path,
            "exception": str(exception),
        },
        status_code=status.HTTP_404_NOT_FOUND,
    )
