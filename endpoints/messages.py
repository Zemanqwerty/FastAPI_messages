from fastapi import APIRouter, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get('/', response_class=HTMLResponse)
async def get_messages(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse('index.html', {'request': request})

@router.websocket('/send')
async def send_message(websocket: WebSocket):
    index_of_element = 0
    await websocket.accept()
    while True:
        message = await websocket.receive_json()
        message_text = message['message_text']
        index_of_element += 1
        
        await websocket.send_json({
            "message_text": message_text,
            "index": index_of_element
        })