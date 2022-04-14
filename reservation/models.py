from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_number = models.IntegerField()
    Date = models.DateField()
    time = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Reservations'
        verbose_name_plural = 'Reservations'
        