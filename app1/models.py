#models.py
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=1000)
    target_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

   
'''
    def get_name_from_url(self):
        parsed_url = urlparse(self.url)
        query_dict = parse_qs(parsed_url.query)
        return query_dict.get('name', [None])[0] or parsed_url.path.split('/')[-1]
'''