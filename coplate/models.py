from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters, validate_retaurant_link
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators = [validate_no_special_characters],
        error_messages={'unique':'이미 사용중인 닉네임입니다.'},
    )
    
    profile_pic = models.ImageField(
        upload_to='profile_pics',
        default = 'default_profile_pic.jpg'
    )
    
    intro = models.CharField(max_length=60, blank=True)
    
    #over-riding
    #AbstractUser는 디폴트로 username을 사용하는데 이메일로 바꿔주기
    def __str__(self):
        return self.email
    
    
class Review(models.Model):
    title = models.CharField(max_length=30)
    restaurant_name = models.CharField(max_length=20)
    restaurant_link = models.URLField(validators=[validate_retaurant_link])
    
    RATING_CHOICES = [
        (1, '★'), #(보이는값, 저장되는값)
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    rating = models.IntegerField(choices = RATING_CHOICES, default=None)

    image1 = models.ImageField(upload_to='review_pics')
    image2 = models.ImageField(upload_to='review_pics', blank=True)
    image3 = models.ImageField(upload_to='review_pics', blank=True)
    content = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title #리뷰를 출력하면 리뷰의 title이 출력됨
