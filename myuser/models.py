from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
USER_CHOICE=[
    ('AMB','Ambulance'),
    ('BLB','Blood-Bank'),
    ('HSP','Hospital'),
    ('MST','Medical-Store'),
]

class Myusermanager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("User must have an email")
        
        user=self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self.db)
        return user


class Myuser(AbstractBaseUser):
    email=models.EmailField(max_length=256,verbose_name="email",unique=True)
    user_type=models.CharField(max_length=3,choices=USER_CHOICE)
    date_joined=models.DateTimeField(verbose_name='date-joined',auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='last-login',auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=Myusermanager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

class City(models.Model):
    std_code=models.PositiveIntegerField(validators=[MaxValueValidator(9999),MinValueValidator(1000)])
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
