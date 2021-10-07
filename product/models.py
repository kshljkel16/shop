from django.db import models

# Create your models here.
from model_utils import Choices
from model_utils.fields import StatusField
from django.contrib.auth import get_user_model

User = get_user_model()


class CreatedatModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    """
    Создание абстрактной модели для добавления поля создания продукта.
    Нужен для сокращения кода и расширяемости
    """
    class Meta:
        abstract = True

class Product(CreatedatModel):
    STATUS = Choices("Available","Not existed")
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products',null=True,blank=True)
    status = StatusField()
    description = models.TextField()

    # products = models.Manager()

    class Meta:
        ordering = ['title','price']

    def __str__(self):
        return self.title

class ProductReview(CreatedatModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews',null=True)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=1)

    # review = ProductReview(product='Edited post,author='Zaida',text='Bad,rating=1)
    # review.product.title,review.product.price

    # product = Product(title='New',price=100,description='Nothing to say',status='Avaible',image=null)