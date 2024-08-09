from django.db import models

# Create your models here.
class Menu(models.Model):
    class Meta: 
        verbose_name = 'menu'
        verbose_name_plural = 'menus'


    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


