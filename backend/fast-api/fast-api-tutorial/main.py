import uvicorn

if __name__ == "__main__" : 
    # app.app:app means folder app -> file app.py ->app = FastAPI
    # 0.0.0.0 means run it on any available domain (local host)

    uvicorn.run("app.app:app", host= "0.0.0.0", port= 8000, reload= True)