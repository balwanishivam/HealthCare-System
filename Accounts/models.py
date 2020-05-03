from django.db import models
from django.contrib.auth.models import User

USER_CHOICE=[
    ('AMB','Ambulance'),
    ('BLB','Blood-Bank'),
    ('HSP','Hospital'),
    ('MST','Medical-Store'),
]

class UserProfile(User):
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    Login_type=models.CharField(max_length=3,choices=USER_CHOICE)

    def __str__(self):
        return self.Login_type

# Create your models here.
