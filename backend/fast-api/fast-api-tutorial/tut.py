from fastapi import FastAPI , HTTPException
from app.schemas import PostCreate , PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
    

app = FastAPI(lifespan= lifespan)

# our API is designed to handle data: accepting requests from frontend or client and returning responses


# setting up the different paths or (endpoints) that we want to have accessible on our api

# Handling posts
# retreive and create new user posts

text_posts = {
    1: {"title": "New Post", "content": "cool test post"},
    2: {"title": "Second Post", "content": "testing fastapi endpoints"},
    3: {"title": "Hello World", "content": "first api response test"},
    4: {"title": "FastAPI RoAcks", "content": "simple in-memory data test"},
    5: {"title": "CRUD Test", "content": "creating posts using fastapi"},
    6: {"title": "Update Test", "content": "checking put and patch requests"},
    7: {"title": "Delete Test", "content": "testing delete endpoint"},
    8: {"title": "Docs Check", "content": "swagger ui is working fine"},
    9: {"title": "Performance", "content": "fast response test post"},
    10: {"title": "Final Test", "content": "everything seems to work"}
}


@app.get("/posts")
def get_all_post(limit: int= None):
    if limit:
        return list (text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code= 404, detail= "Post not founf")
    return text_posts.get(id)


'''
creating a post is something different than getting a post
in fastapi has automatic data validaation which means it's going to check the data that's being sent into the function to make sure it's accurate.
Now up until this point, we looked at the query parameters and the path parameters. But there's another way that we can send data to our API.
And it's by using something called the request body okay. The body is kind of like more hidden information.

It's not directly inside of the URL. It's in the field called body. And the way that we accept that type of data is by creating something called a schema in fast API.
'''
@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse : 
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) +1] = new_post
    return new_posts