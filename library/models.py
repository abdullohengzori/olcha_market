# from django.db import models
# class TimeStampedModel(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     class Meta:
#         abstract = True
# class User(TimeStampedModel):
#     username = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=100)
#     def __str__(self):
#         return self.first_name
# class Shop(TimeStampedModel):
#     holat = (
#         ('basic', 'basic'),
#         ('premium', 'premium'),
#     )
#     turi = models.CharField(default='basic', choices=holat, max_length=100)
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     address = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name
# class Product(TimeStampedModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop')
#     # user = models.ManyToManyField(User, related_name='user')
#     # shop = models.ManyToManyField(Shop, related_name='shop')
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
#     # shop = models.OneToOneField(Shop, on_delete=models.CASCADE, related_name='shop')
#     buy = models.DateField(auto_now_add=True)


from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
class User(TimeStampedModel):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name
    class Meta:
        db_table = 'user'
        verbose_name = 'abdulloh'
        verbose_name_plural = 'abdullohlar'
        # unique_together = ('username',)
        constraints = [
            UniqueConstraint(
                Lower('username'),
                name='iltimos boshqa narsa yooooz'
            )
        ]

class Shop(TimeStampedModel):
    holat = (
        ('basic', 'basic'),
        ('premium', 'premium'),
    )
    turi = models.CharField(default='basic', choices=holat, max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Product(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop')
    buy = models.DateField(auto_now_add=True)