from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
from routers import author, router_example, bookstore

app = FastAPI(
    title="My Awesome API",
    summary="A brief summary of what this API does",
    description="A more detailed description of the API functionality",
    version="1.0.0",
    debug=True
)


# It intercepts the exception after it is raised but before the response is sent back to the client.
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "OOPs! something went wrong"
        },
    )


app.include_router(router_example.router, prefix="/router_eg")
app.include_router(bookstore.router, prefix="/books")
app.include_router(author.router, prefix="/author")


@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.get("/error_endpoint")
async def raise_exc():
    raise HTTPException(status_code=400)