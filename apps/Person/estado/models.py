from django.db import models


# Create your models here.

class Estado(models.Model):
    class Meta:
        verbose_name = 'Estado'
        db_table = 'person_estado'

    is_active = models.BooleanField(default=True, blank=False, null=False, db_index=True)

    def __str__(self):
        return f"Estado activo: {self.is_active}"



