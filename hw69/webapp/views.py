from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

