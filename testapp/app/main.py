import os
from datetime import datetime

import fastapi.responses
import uvicorn
from typing import Optional
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 

app = FastAPI()


@app.get("/tailwind/")
async def read_index():
    return FileResponse('play-tailwind-main/index.html')


app.mount("/tailwind/", StaticFiles(directory="play-tailwind-main"), name="static")


@app.get("/", response_class=fastapi.responses.HTMLResponse)
def read_root():
    return '''
<html>
<body style="display: flex; align-items: center; justify-content: center; background-color: #edf4ff;">
    <div style="text-align: center; padding-bottom: 150px">
        <h3> Hello World </h3>
        <h5><a href="/logout">Logout</a></h5>
        <br /><br /><br /><br />
    </div>
</body>
</html>
    '''


@app.get("/hello")
def read_root():
    return {
        "Hello": "World",
        "logout": "/logout"
    }


ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_VALUE = os.environ['ACCESS_TOKEN_VALUE']


@app.get("/auth")
async def auth(request: Request):
    if (ACCESS_TOKEN_KEY in request.headers) and (request.headers[ACCESS_TOKEN_KEY] == ACCESS_TOKEN_VALUE):
        return "okay"
    else:
        raise HTTPException(status_code=401, detail="You are not logged in.")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}




@app.get("/test/get")
def testGetEndpoint(request: Request):
    print("Inside testGetEndpoint")
    return inspectRequest(request)

@app.post("/test/post")
def testPostEndpoint(request: Request):
    print("Inside testPostEndpoint")
    return inspectRequest(request)

def inspectRequest(request: Request):
    hmini = {};
    for h in request.headers:
        if len(request.headers[h]) < 100 :
            hmini[h] = request.headers[h]

    print(f'    {request.url.path} : {hmini}')
    return {
        "path": request.url.path,
        "time": datetime.now(),
        "headers": hmini
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


