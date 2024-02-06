from brands.models import *
from product.models import *
from home.models import *
def navbar(request):
    brandsitems = brandsitem.objects.all()
    productitem = products.objects.all()
    adss = ads.objects.order_by('?').first()
    return {'brandsitem': brandsitems,"productitem":productitem,'adss':adss}