from .models import Catagory
def all_catagories(request):
     return{
          'all_catagories' : Catagory.objects.all()
     }