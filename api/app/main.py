from fastapi import FastAPI
from api.app.routes import router
from api.app.middleware import setup_middleware

app = FastAPI(title="RAG LATAM Politics API")

setup_middleware(app)
app.include_router(router)
