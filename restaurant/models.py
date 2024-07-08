from django.db import models

# Create your models here.
class BookingTable(models.Model):
    ID = models.IntegerField(),
    Name = models.CharField(max_length=255),
    No_of_guests = models.IntegerField(),
    BookingDate = models.DateField()



class MenuTable(models.Model):
    ID = models.IntegerField(),
    Title = models.CharField(max_length=255),
    Price = models.DecimalField(max_length=10,decimal_places=2),
    Inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
