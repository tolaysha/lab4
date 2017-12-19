from django.db import models


# Create your models here.
class Subscribers(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
            return 'Email:%s,  Name:%s' % (self.email, self.name)
    class Meta:
        verbose_name = 'Sub'
        verbose_name_plural ='Subs'


