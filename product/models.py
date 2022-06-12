from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    # VARIANTS = (
    #     ('None', 'None'),
    #     ('Size', 'Size'),
    #     ('Color', 'Color'),
    #     ('Size-Color', 'Size-Color'),
    #
    # )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # many to one relation with Category
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    amount = models.IntegerField(default=0)
    minamount = models.IntegerField(default=3)
    # variant = models.CharField(max_length=10, choices=VARIANTS, default='None')
    # detail=RichTextUploadingField()
    slug = models.SlugField(null=True, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title