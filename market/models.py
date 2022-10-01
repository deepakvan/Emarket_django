from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,null=False,unique=True)
    desc=models.CharField(max_length=1000,null=True)
    features=models.CharField(max_length=1000,null=True) # json or dictionary object
    category=models.CharField(max_length=1000,null=True)
    price=models.FloatField(null=False)
    image = models.ImageField(upload_to='product_images')
    discount_price = models.FloatField(null=False)

class Wish_products(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    User_id = models.ForeignKey('User',on_delete=models.CASCADE)

class Ordered_products(models.Model):
    id = models.IntegerField(primary_key=True)
    status=models.CharField(max_length=50,null=False)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    User_id = models.ForeignKey('User', on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    pincode=models.IntegerField()
    mobile_no=models.CharField(max_length=12)



class Product_pictures(models.Model):
    id=models.IntegerField(primary_key=True)
    picture=models.ImageField(upload_to='product_images')
    p_id=models.ForeignKey('Product',on_delete=models.CASCADE)