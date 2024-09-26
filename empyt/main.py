import os
import re
from io import StringIO
import jinja2
from django.template import engines, TemplateDoesNotExist

class EmpytEngine:
    """
    A template engine that processes templates with inline Python code.
    It uses Jinja2 or Django templating to handle includes, extends, and standard syntax.
    """

    def __init__(self, template_dir=None, engine='jinja'):
        self.template_dir = template_dir or '.'

        if engine == 'jinja':
            self.jinja_env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(self.template_dir),
                autoescape=True
            )
            self.engine = 'jinja'
        elif engine == 'django':
            self.engine = 'django'
            self.django_engine = engines['django']

    def render(self, template_name, context=None):
        if context is None:
            context = {}

        # Step 1: Use the specified engine to process the template
        try:
            if self.engine == 'jinja':
                jinja_template = self.jinja_env.get_template(template_name)
                rendered_template = jinja_template.render(context)
            elif self.engine == 'django':
                django_template = self.django_engine.get_template(template_name)
                rendered_template = django_template.render(context)
            else:
                return

        except (TemplateDoesNotExist, Exception) as e:
            # Handle errors, but for now we will just print them
            print(f"Template processing error: {e}")
            return ''

        # Step 2: Process inline Python code in the resulting output
        processed_content = self._execute_python(rendered_template, context)

        return processed_content

    def _execute_python(self, content, context):
        """
        Preprocess custom Python code blocks in the rendered template.
        """
        buffer = StringIO()
        context['buffer'] = buffer  # Include buffer in the execution context

        def exec_python(match):
            code = match.group(1)
            code = self._correct_indentation(code)
            if code:
                exec(f"import sys\nold_stdout = sys.stdout\nsys.stdout = buffer\n{code}\nsys.stdout = old_stdout", context)
            result = buffer.getvalue()
            buffer.truncate(0)
            return result

        def eval_python(match):
            expression = match.group(1).strip()
            result = eval(expression, context)
            return str(result)

        # Execute custom Python code blocks with <%%> and %%%%
        content = re.sub(r'<%([\s\S]+?)%>', exec_python, content)
        content = re.sub(r'%%([^}]+?)%%', eval_python, content)

        return content

    def _correct_indentation(self, code):
        """
        Correct the indentation for multi-line Python code blocks.
        """
        lines = code.splitlines()
        min_indent = min((len(line) - len(line.lstrip()) for line in lines if line.strip()), default=0)
        return '\n'.join(line[min_indent:] for line in lines)
