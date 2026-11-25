from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Andriy Burkikov",
        "title": "100 days of Machine Learning",
        "content": "Machine Learning is a fascinating field that allows us to build intelligent systems.",
        "date_posted": "April 21, 2025",
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>Hello, World! Shubham here</h1>"


@app.get("/api/posts") 
def get_posts():
    return {"data": posts}
