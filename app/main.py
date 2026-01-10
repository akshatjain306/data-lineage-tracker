from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import router

app = FastAPI(title="Data Lineage Tracker")

Base.metadata.create_all(bind=engine)

app.include_router(router)
