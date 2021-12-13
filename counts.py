from .models import Fisherman, Retailer

total_fishermen = Fisherman.objects.all().len()
registered_retailers = Retailer.objects.get().filter(licensed=True).len()

