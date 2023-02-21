from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app1.models import Product
from django.core.mail import send_mail

import requests
from bs4 import BeautifulSoup as bs

class Command(BaseCommand):
    help = 'Sends email to all users who have products with a price drop'

    def handle(self, *args, **options):
        users = User.objects.all()
        users = User.objects.filter(is_superuser=False)

        for user in users:
            products = Product.objects.filter(user=user)
            if products.exists():
                for product in products:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Connection': 'keep-alive'
                    }
                    page=requests.get(product.url,headers=headers)
                    soup = bs(page.content,"html.parser")

                    try:
                        actual_price = soup.find('span', attrs={'class': 'a-price-whole'}).get_text()
                        actual_price = float(actual_price.replace(",", ""))
                    except:
                        actual_price = "Out of Stock"
                    
                    if actual_price != "Out of Stock":
                        if product.target_price<=actual_price:
                            print(f"Sending email to {user.email} for Product: {product.name}, URL: {product.url}, Target Price: {product.target_price} ,Actual Price: {actual_price}")
                            # Send the email to the user's email address
                            send_mail(
                                f'Price of {product.name} dropped on Amazon. Check it out!', #email subject
                                f'Hello {user.username},\n\nYour price of product on amazon is dropped Shop now. \n\n Url: {product.url}', # email message
                                'mashymalii@gmail.com', 
                                [user.email], #user's email address
                                fail_silently=False,
                            )


