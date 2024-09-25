# myapp/views.py
from django.http import HttpResponse
from django.views import View
from empyt import EmpytEngine

# Initialize the template engine
template = EmpytEngine(template_dir='./templates', engine="django")

# Function-based view
def index(request):
    context = {
        'some_var': True,
        'another_var': False
    }
    content = template.render("index.html", context)
    return HttpResponse(content)

# Class-based view
class IndexView(View):
    def get(self, request):
        context = {
            'some_var': True,
            'another_var': False
        }
        content = template.render("index.html", context)
        return HttpResponse(content)
