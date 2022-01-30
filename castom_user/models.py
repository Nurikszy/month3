from django.db import models
from django.contrib.auth.models import User

ADMIN = 1
VIPCLIENT = 2
KLIENT = 3
user_type = (
    (ADMIN, 'ADMIN'),
    (VIPCLIENT, 'VIPCLIENT'),
    (KLIENT, 'CLIENT'),
)
MALE = 1
FEMALE = 2
OTHER = 3
gender_type = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
    (OTHER, 'OTHER'),
)

class CastomUser(User):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
    user_type = models.IntegerField(choices=user_type,
                                    verbose_name='тип пользователя',
                                    default=KLIENT)
    number = models.CharField('phone number',max_length=40)
    age = models.IntegerField()
    gender = models.IntegerField(choices=gender_type, verbose_name='Гендер')