from django.shortcuts import render , get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404

from django.http import  HttpResponse

def home(request):
    return render(request, 'dashboard/home.html')

def about(request):
    return render(request, 'dashboard/about.html')

def query_list(request):
    ctx = {"queries" : Queries}
    return render(request, 'dashboard/query_list.html', ctx)

def query_details(request , slug):
    item = next((x for x in Queries if x['slug'] == slug), None)
    if not  item :
        raise Http404("آیتم یافت نشد")
    return render(request, 'dashboard/query_detail.html', {"q": item})

def book_list(request):
    ctx = {'book_list':books}
    return render(request, 'dashboard/book_list.html', ctx)

Queries = [
    {
        "slug": "monthly-sales",
        "title": "فروش ماهانه",
        "description": "جمع فروش به تفکیک ماه",
        "sample_sql": "SELECT month, SUM(amount) FROM sales GROUP BY month;"
    } ,
    {
        "slug": "top-5-products",
        "title": "۵ محصول برتر",
        "description": "بیشترین فروش بر اساس مبلغ",
        "sample_sql": "SELECT product, SUM(amount) as total FROM sales GROUP BY product ORDER BY total DESC LIMIT 5;",
    }
]

books = [
    {
        "slug": "SL1",
        "title": "T1",
        "author": "A1",
        "summary": "S1",
    },
    {
        "slug": "SL2",
        "title": "T2",
        "author": "A2",
        "summary": "S2",
    }
]