# empyt

AKA: embedded python (for html) templating.

For far too long, python web frameworks have pushed for "separation of concerns". No longer.

Crafted in honor of mod_python, erb, and php, and the like. Compatible with Flask, FastAPI, Django, and any Python WSGI server.

## Quick Start
To get started with empyt, follow these steps:

1. Install empyt (assuming it's available on PyPI):
    ```bash
    pip install empyt
    ```

2. In your Python web application, import and initialize the EmpytEngine:

   ```python
   from empyt import EmpytEngine

   template_engine = EmpytEngine(template_dir='path/to/your/templates', engine='jinja')
   ```

3. Create a template file (e.g., `example.html`) in your templates directory:

   ```html
   <html>
   <body>
     <h1>Hello, %% name %%!</h1>
     <% for i in range(3):
        print(f"<p>This is paragraph {i+1}</p>")
     %>
   </body>
   </html>
   ```

4. Render the template in your view function:

   ```python
   @app.route('/')
   def hello():
       context = {'name': 'World'}
       return template_engine.render('example.html', context)
   ```

## Overview

empyt is a template library that allows you to embed Python code directly into your HTML templates.

Key features:
- Allows direct usage of Python code and syntax within templates
- Compatibile with any additional template engine like Jinja, Django, etc.
- Compatible with any Python web server of framework (Flask, FastAPI, Django, etc.)

## Syntax
empyt uses standard Python syntax within its code blocks. There's no custom templating language to learn.

### Evaluation
Use `%% expression %%` to evaluate a Python expression and echo its result.
Evaluation uses the built-in `eval` method.

```html
<p>The current year is %% datetime.now().year %%</p>
```

### Execution
Use `<% code %>` for multi-line Python code blocks.
Execution uses the built-in `eval` method.

Here, echo the result directly to the DOM using `print()`.
```html
<%
items = [1,2,3,4,5]
for item in items:
    print(f"<li>{item}</li>")
%>
```

Alternatively, move the loop into a function, and get its value later in the page.
```html
<%
items = [1,2,3,4,5]
def set_list():
    output = ""
    for item in items:
        output += f"<li>{item}</li>"
    return output
%>

<ul>
    %% set_list() %%
</ul>
```

### Loops
You can use standard Python loops within execution blocks:

```html
<ul>
<% for i in range(5):
    print(f"<li>Item {i+1}</li>")
%>
</ul>
```

### Conditionals
Conditionals can be used similarly to loops:

```html
<%
if user.is_authenticated:
    text = f"Welcome.${user.username}"
else:
    text = "Please log in"
%>
<p>%% text %%</p>
```

### Ternaries
Ternaries can be easily crafted with the `%% %%` expression syntax. This is especially useful for quick, one-line render statements.
```html
<% example_switch = "on" %>
%% "<h1>Switch is off</h1>" if example_switch == "off" else "<h1>Switch is on</h1>" %%
```

## Examples
For more specific examples, refer to:
- [Django Example](./examples/django_example.py)
- [FastAPI Example](./examples/fastapi_example.py)
- [Flask Example](./examples/flask_example.py)

## Similar Projects
- [Genshi](https://genshi.readthedocs.io/en/latest/templates/): A Python-based templating toolkit for generation of web-aware output.
- [Kid](https://www.turbogears.org/1.0/docs/GettingStarted/Kid.html): A simple templating language for XML based vocabularies written in Python.
