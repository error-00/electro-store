from django.db.models import Q
from main.models import Product

def q_search(query):
    keywords = [word for word in query.split() if len(word) > 2]
    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)
    
    return Product.objects.filter(q_objects)
