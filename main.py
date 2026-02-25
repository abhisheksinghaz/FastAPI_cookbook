from fastapi import FastAPI, HTTPException
from sql_example.database import engine, Base
from sql_example.user_table import User
from routers import author, router_example, bookstore, user

app = FastAPI()


@app.on_event("startup")
def on_startup():
    # Create any missing tables defined in SQLAlchemy models (idempotent)
    Base.metadata.create_all(bind=engine)


app.include_router(router_example.router, prefix="/router_eg")
app.include_router(bookstore.router, prefix="/books")
app.include_router(author.router, prefix="/author")
app.include_router(user.router, prefix="/user")


@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.get("/error_endpoint")
async def raise_exc():
    raise HTTPException(status_code=400)