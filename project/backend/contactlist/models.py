from django.db import models
from taggit.managers import TaggableManager


class ContactGroup(models.Model):
    name = models.CharField(max_length=100)


class Addresses(models.Model):
    group = models.ManyToManyField(ContactGroup)
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='OWNER')
    tag = TaggableManager(blank=True)
    
    class Meta:
        ordering = ['created']

    profile_photo = models.ImageField(blank=True, null=True)
    company = models.CharField(blank=True, max_length=50)
    dept = models.CharField(blank=True, max_length=50)
    position = models.CharField(blank=True, max_length=50)
    tel_number = models.CharField(blank=True, max_length=255)
    fax_number = models.CharField(blank=True, max_length=255)
    email = models.CharField(blank=True, max_length=255)
    website = models.URLField(blank=True)

    GENDER_CHOICES = [
        ('M', '남자'),
        ('F', '여자'),
        ('C', 'Custom'),
    ]
    birthday = models.DateField(null=True)
    # age = models.CharField(blank=True, max_length=3)  # 나이
    bio = models.TextField(blank=True)  # 경력, 세부조정 필요
    gender = models.CharField(blank=True, choices=GENDER_CHOICES, max_length=30)  # 성별
    like = models.CharField(blank=True, max_length=30)  # 좋아하는 것
    dislike = models.CharField(blank=True, max_length=30)  # 싫어하는 것