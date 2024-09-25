"""
Note: There are multiple options for django integration. Any one of these will work.
- Per project
- Per view (function based)
- Per view (class based)
"""

"""
Settings
"""
# settings.py
import os
from django.conf import settings
from empyt.templating import InlinePythonTemplate

# Define the InlinePythonTemplate engine
class InlinePythonTemplateEngine:
    def __init__(self, template_dir=None):
        self.template = InlinePythonTemplate(template_dir=template_dir)

    def get_template(self, template_name):
        return self.template.render(template_name)

# Add the custom template engine to the settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Keep the default Django template backend
        'DIRS': [os.path.join(BASE_DIR, 'myapp/templates')],  # Specify your template directories
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Default context processors
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'inline_python_template': InlinePythonTemplateEngine,  # Add your custom template engine
            },
        },
    },
]


"""
Function-based view
"""
from django.http import HttpResponse
from empyt.templating import InlinePythonTemplate

# Initialize the template engine
template = InlinePythonTemplate(template_dir='myapp/templates', engine='django')

def index(request):
    context = {
        'some_var': True,
        'another_var': False
    }
    content = template.render("examples/index.html", context)
    return HttpResponse(content)


"""
Class-based view
"""
from django.views import View
from django.http import HttpResponse
from empyt.templating import InlinePythonTemplate

# Initialize the template engine
template = InlinePythonTemplate(template_dir='myapp/templates', engine='django')

class IndexView(View):
    def get(self, request):
        context = {
            'some_var': True,
            'another_var': False
        }
        content = template.render("examples/index.html", context)
        return HttpResponse(content)
