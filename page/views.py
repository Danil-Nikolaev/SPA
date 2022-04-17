from django.shortcuts import render
from django.views.generic import ListView
from page.models import SPA
# Create your views here.


class PageList(ListView):
    model = SPA
    template_name = "SPA_List.html"
    context_object_name = "spa_list"

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        return ordering
