from typing import List
from threading import Thread
from src.dashboard import app_dash
import uvicorn
from fastapi import FastAPI
from src.responses import TrendItem
from src.services import get_trends, save_trends

app = FastAPI()


@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    return get_trends()

def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)

def run_dash():
    app_dash.run_server(debug=True, use_reloader=False)

if __name__ == "__main__":
    trends = get_trends()

    if not trends:
        save_trends()

    fastapi_thread = Thread(target=run_fastapi)
    dash_thread = Thread(target=run_dash)

    fastapi_thread.start()
    dash_thread.start()

    fastapi_thread.join()
    dash_thread.join()
