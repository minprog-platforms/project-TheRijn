from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watching = models.ManyToManyField("Listing", related_name="watched_by")


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    starting_bid = models.DecimalField(
        max_digits=14, decimal_places=2, default=Decimal("0.00")
    )
    _image_url = models.URLField(blank=True, null=True)
    categories = models.ManyToManyField("Category", related_name="listings")
    closed = models.BooleanField(default=False)

    @property
    def image_url(self):
        return self._image_url if self._image_url else ""

    @image_url.setter
    def image_url(self, value):
        self._image_url = value

    def __str__(self):
        return f"{self.title} by {self.user}"


class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    price = models.DecimalField(max_digits=14, decimal_places=2)


class Comment(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"
