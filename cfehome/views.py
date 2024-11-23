from django.http import HttpResponse
from django.shortcuts import render
from visits.models import Page_Visit

def home_view(request,*args,**kwargs):
    return about_view(request,*args,**kwargs)


def about_view(request, *args, **kwargs):
    qs = Page_Visit.objects.all()
    page_qs = Page_Visit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0
    my_title = "My page"
    my_context = {
        "page_title" : my_title,
        "page_visits_count" : page_qs.count(),
        "percent" : percent,
        "total_visit_count" : qs.count()
    }
    html_template = "home.html"
    Page_Visit.objects.create(path = request.path)
    return render(request, html_template ,my_context)
    