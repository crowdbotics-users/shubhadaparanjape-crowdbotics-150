from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'django-oscar', 'url': 'http://pypi.python.org/pypi/django-oscar/1.5.1'},
	{'name':'satchless', 'url': 'http://pypi.python.org/pypi/satchless/1.1.3'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
