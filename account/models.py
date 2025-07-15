from django.db import models
from django.contrib.auth.models import User, AbstractUser


class CustomerUser(AbstractUser):
    phone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'auth_user'
