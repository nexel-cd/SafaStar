from brands.models import *
from product.models import *

def navbar(request):
    brandsitems = brandsitem.objects.all()
    product = products.objects.all()
    return {'brandsitem': brandsitems,"product":product}