from fastapi import FastAPI
import routers.rts as MongoRouter
import uvicorn

app = FastAPI(    
    title='MongoDB API',
    version='0.0.1',
    description='Personal project with FastAPI')
app.include_router(MongoRouter.app, tags=['mongo'])

if __name__ == '__main__':
  
    uvicorn.run("main:app", host="0.0.0.0", port=8003)