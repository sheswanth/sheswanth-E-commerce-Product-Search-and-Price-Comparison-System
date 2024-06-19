from django.db import models


# Define choices for property categories


class Product(models.Model):
    id = models.AutoField(blank=False, primary_key=True)
    product_title = models.CharField(max_length=200)
    product_description = models.TextField()
    amazon_price = models.DecimalField(max_digits=10, decimal_places=2)
    amazon_link = models.URLField()
    flipkart_price = models.DecimalField(max_digits=10, decimal_places=2)
    flipkart_link = models.URLField()
    product_images = models.ImageField(upload_to='products/static/images', blank=True, null=True)

    def str(self):
        return self.product_title
