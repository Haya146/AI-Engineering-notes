from fastapi import FastAPI , HTTPException, File, UploadFile, Form, Depends
from app.schemas import PostCreate , PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
from app.images import imagekit

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
    


app = FastAPI(lifespan= lifespan)

# allows me to create a post when I upload a file
@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...), 
    caption: str = Form (""),
    session: AsyncSession = Depends(get_async_session)
):
    post = Post(
        caption=caption,
        url="dummy url",
        file_type="photo",
        file_name= "dummy name"
    )
    session.add(post) # add to the database
    await session.commit()
    await session.refresh(post)
    return post
    
@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
):
    # to get posts in feed by order it by descending by created time
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()] # turninh posts to a list to access them all at once, it's due to the way that fastapi returns the results (returns a cursor object)
    
    posts_data =[]
    for post in posts:
        posts_data.append(
            {
                "id":str(post.id),
                "caption": post.caption,
                "url": post.url,
                "file_type":post.file_type,
                "file_name": post.file_name,
                "created_at": post.created_at
            }
        )
        
    return {"posts": posts_data}