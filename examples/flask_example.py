from flask import Flask, Response
from empyt import EmpytEngine

app = Flask(__name__)
template = EmpytEngine(template_dir='examples/templates', engine='jinja')

@app.route('/')
def index():
    context = {
        'some_var': True,
        'another_var': False
    }
    content = template.render("index.html", context)

    return Response(content, content_type='text/html')

if __name__ == '__main__':
    app.run(debug=True)
