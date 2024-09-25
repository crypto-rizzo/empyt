# empyt
AKA: embedded python (for html) templating. Crafted in in honor of mod_python, erb, and php, and the like.

For too long web frameworks have pushed for "separation of concerns".

Compatibile with Flask, FastAPI, Django, and any Python WSGI server.

## Basic usage
```py
from empyt import empyt

app = FastAPI()
template = InlinePythonTemplate(template_dir='examples/templates', engine='jinja')


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

```

For more specific examples
- [Django Example](./examples/django_example.py)
- [FastAPI Example](./examples/fastapi_example.py)
- [Flask Example](./examples/flask_example.py)


## Similar Projects
I didn't do a ton of research beforehand as I normally do, but as always, some cool projects doing similar things:
- https://genshi.readthedocs.io/en/latest/templates/
- https://www.turbogears.org/1.0/docs/GettingStarted/Kid.html
