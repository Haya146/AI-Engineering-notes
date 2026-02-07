### Package Manager
 -> 1- pip
 -> 2- uv
     - uv init . 
     (this set all of the dependencies for this particular project)
### install dependincies
     - uv add fastapi
     - uv add python-dotenv
     - uv add fastapi-users[sqlalchemy] 
            ### we're going to use when we start handling the authentication and the authorization in our project
     - uv add imagekitio
            ### we are going to use to handle our images and videos
     - uv add uvicorn[standard]
            ###uvicorn: is a web server in python that allow us to serve our fast API appliccation
     - uv add aiosqlite
            ### we are going to use this for interacting with our database

### run the fast api 
     - uv run .\main.py
     - then change this link http://0.0.0.0:8000/ to http://localhost:8000/
   