from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # avoid duplicate favorites

    def __str__(self):
        return f"{self.user.username} favorited {self.product.name}"

