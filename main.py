from fastapi import FastAPI
import uvicorn
from endpoints import messages
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='FastAPI ws')
app.include_router(messages.router, prefix='')
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)