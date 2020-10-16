from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand_name




class Product(models.Model):

    CONDITION_TYPE = (
        ("New","New"),
        ("Used","Used")
    )

    title = models.CharField(max_length = 100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    decrtiption = models.TextField()
    condition = models.CharField(max_length=200, choices=CONDITION_TYPE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwarws):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwarws)

    def __str__(self):
        return self.title



class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.title