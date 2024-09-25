from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from empyt import EmpytEngine

app = FastAPI()
template = EmpytEngine(template_dir='examples/templates', engine='jinja')


@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Load and render the template using InlinePythonTemplate
    context = {
        'some_var': True,
        'another_var': False
    }
    content = template.render("index.html", context)
    return Response(content, media_type='text/html')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
