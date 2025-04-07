from django.db import models

#Create your models here.
class Product(models.Model):
    Product_id = models.AutoField
    Product_name = models.CharField(max_length=50)
    category = models.CharField( max_length=50, default="")
    subcategory = models.CharField(max_length=50 ,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_datd = models.DateField()
    image = models.ImageField(upload_to="shop/images" ,default="")

    def __str__(self):
        return self.Product_name
    


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
    

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default='', null=True, blank=True)
    address = models.CharField(max_length=111)
    landmark = models.CharField(max_length=111, default='')
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE,default="1")
    update_desc = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:10]+"..."

#auto_now_add= True :- when the object is first create it set the field automatically.