from datetime import datetime
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root(bg: str = Query(default="white", description="Цвет фона")):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>TIME</title>
</head>
<body style="background-color:{bg}; font-family:sans-serif;
           display:flex; justify-content:center; align-items:center;
           height:100vh; margin:0;">
    <h1 style="font-size:4em;">{now}</h1>
</body>
</html>"""
    return html
