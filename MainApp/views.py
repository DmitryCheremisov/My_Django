from django.shortcuts import render
from django.shortcuts import HttpResponse, Http404
from .models import Item

user_data = {
    "surname": "Иванов",
    "name": "Алексей",
    "second_name": "Петрович"
}

items = [
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]

# Create your views here.
def about(request):
    return HttpResponse("Это о компании...")

def item_list(request):
    items = Item.objects.all()
    context = {"items" : items}
    return render(request, 'items_list.html', context)

def main(request):
    #items = Item.objects.all()
    return render(request, 'index.html', context=user_data)

def db_list(request):
    items = Item.objects.all()
    context = {"items" : items}
    return render(request, 'DB_items.html', context)

def item(request, id):
    items = Item.objects.all()
    context = {}
    for item in items:
        if item["id"] == id:
            context["item"] = item
            return render(request, 'item.html', context)
    raise Http404
