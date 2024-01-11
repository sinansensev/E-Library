#from itertools import product
from multiprocessing.sharedctypes import Value
from sqlite3 import Date
from statistics import mode
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here. 


def generate_custom_id():
    
    return 1000 + books.objects.count()    


class CustomIDMixin(models.Model):
    custom_id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_id)

    class Meta:
        abstract = True   

def generate_custom_idcocuk():
    
    return 2000 + cocukkitabi.objects.count()    


class CustomIDMixin(models.Model):
    custom_id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_idcocuk)

    class Meta:
        abstract = True       
def generate_custom_idgerilim():
    
    return 3000 + gerilim.objects.count()    


class CustomIDMixin(models.Model):
    custom_id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_idgerilim)

    class Meta:
        abstract = True       

def generate_custom_idmacera():
    
    return 4000 + macera.objects.count()    


class CustomIDMixin(models.Model):
    custom_id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_idmacera)

    class Meta:
        abstract = True       

def generate_custom_idaksiyon():
    
    return 5000 + aksiyon.objects.count()    


class CustomIDMixin(models.Model):
    custom_id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_idaksiyon)

    class Meta:
        abstract = True       

def generate_custom_idbiyografik():
    
    return 6000 + biyografik.objects.count()    


class CustomIDMixin(models.Model):
    custom_id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_idbiyografik)

    class Meta:
        abstract = True       

def generate_custom_ideducation():
    
    return 7000 + education.objects.count()    


class CustomIDMixin(models.Model):
    custom_id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_ideducation)

    class Meta:
        abstract = True       


class books(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_id)
    name = models.CharField(max_length=80)
    detail = models.CharField(max_length=10000)
    review = models.CharField(max_length=1000,default="-")
    rate = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pdf =models.FileField(null=True, blank=True)
    catid = models.IntegerField(default=1) 
    image = models.ImageField(null=False, blank=True)
    author = models.TextField(max_length=50,null=True, blank=True)

    

class cocukkitabi(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_idcocuk)
    name = models.CharField(max_length=80)
    detail = models.CharField(max_length=10000)
    review = models.CharField(max_length=1000,default="-")
    rate = models.  FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pdf =models.FileField(null=True, blank=True)
    catid = models.IntegerField(default=2)
    image = models.ImageField(null=False, blank=True)
    author = models.TextField(max_length=50,null=True, blank=True)

class gerilim(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_idgerilim)
    name = models.CharField(max_length=80)
    detail = models.CharField(max_length=10000)
    review = models.CharField(max_length=1000,default="-")
    rate = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pdf =models.FileField(null=True, blank=True)
    catid = models.IntegerField(default=3) 
    image = models.ImageField(null=False, blank=True)
    author = models.TextField(max_length=50,null=True, blank=True)

class macera(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_idmacera)
    name = models.CharField(max_length=80)
    detail = models.CharField(max_length=10000)
    review = models.CharField(max_length=1000,default="-")
    rate = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pdf =models.FileField(null=True, blank=True)  
    catid = models.IntegerField(default=4) 
    image = models.ImageField(null=False, blank=True)
    author = models.TextField(max_length=50,null=True, blank=True)


class aksiyon(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_idaksiyon)
    name = models.CharField(max_length=80)
    detail = models.CharField(max_length=10000)
    review = models.CharField(max_length=1000,default="-")
    rate = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pdf =models.FileField(null=True, blank=True)  
    catid = models.IntegerField(default=5) 
    image = models.ImageField(null=False, blank=True)
    author = models.TextField(max_length=50,null=True, blank=True)


class biyografik(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_idbiyografik)
    name = models.CharField(max_length=80)
    detail = models.CharField(max_length=10000)
    review = models.CharField(max_length=1000,default="-")
    rate = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pdf =models.FileField(null=True, blank=True)
    catid = models.IntegerField(default=6)   
    image = models.ImageField(null=False, blank=True)
    author = models.TextField(max_length=50,null=True, blank=True)


class education(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_ideducation)
    name = models.CharField(max_length=80)
    detail = models.CharField(max_length=10000)
    review = models.CharField(max_length=1000,default="-")
    rate = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pdf =models.FileField(null=True, blank=True)
    catid = models.IntegerField(default=7) 
    image = models.ImageField(null=False, blank=True)
    author = models.TextField(max_length=50,null=True, blank=True)


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('cocukkitabi', 'Çocuk Kitabı'),
        ('gerilim', 'Gerilim'),
        ('macera', 'Macera'),
        ('aksiyon', 'Aksiyon'),
        ('education','Egitim'),
        ('biyografik', 'Biyografik'),
        ('books','Bilim Kurgu')
    ]
    id = models.PositiveBigIntegerField(primary_key=True, default=generate_custom_ideducation)
    name = models.CharField(max_length=80)
    detail = models.CharField(max_length=10000)
    rate = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    pdf = models.FileField(null=True, blank=True)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='books')
    image = models.ImageField(null=False, blank=True)
    author = models.TextField(max_length=50,null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.id:
            last_id = Book.objects.order_by('-id').first()
            self.id = 1 if last_id is None else last_id.id + 1
        super(Book, self).save(*args, **kwargs)


"""class Product(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book', null=True,blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()"""
