from django.db import models
from profiles.models import UserProfile

APPROVAL = ((0, "Awaiting Moderation"), (1, "Approved"))
# Create your models here.


class Category (models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product (models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review (models.Model):

    reviewer = models.ForeignKey(UserProfile,
                                 on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    review_content = models.TextField(null=False, blank=False)
    approved = models.IntegerField(choices=APPROVAL, default=0)

    def __str__(self):
        return f'Comment posted by: {self.reviewer}'
