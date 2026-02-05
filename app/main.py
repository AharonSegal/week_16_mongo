from fastapi import FastAPI

from app.routs import router
from app.fill_data import fill_data_if_empty

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
def startup():
    fill_data_if_empty()