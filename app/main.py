import logging
import uvicorn
from fastapi import FastAPI
from app.api import generate


log = logging.getLogger(__name__)

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(
        generate.router, prefix='/generate', tags=['generate']
    )

    return application

app = create_application()

@app.on_event('startup')
async def startup_event():
    log.info('Starting up...')

@app.on_event('shutdown')
async def shutdown_event():
    log.info('Shutting down...')

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)