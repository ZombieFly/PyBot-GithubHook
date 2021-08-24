from fastapi import FastAPI,Request
import requests
from time import sleep
import uvicorn

from handle import Handle

import config

app=FastAPI()

print('webhook is running')
async def sendNbMessage(group_id: list, message):
    for gid in group_id:
        response = requests.get(url=f'{config.gocq_url}send_group_msg?group_id={gid}&message={message}')
        print(response.text)
        sleep(config.cycule_time)

@app.post(config.api_url)
async def recWebHook(req: Request, group_id= config.group_id):
    body = await req.json()
    event = req.headers.get("X-Github-Event")
    try:
        message = getattr(Handle, event)(body)
    except:
        message= ''
    if message != '':
        await sendNbMessage(group_id, message)

uvicorn.run(app = app, host = config.host, port = config.port)
