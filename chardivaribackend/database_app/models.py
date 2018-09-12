from django.db import models
import datetime



class House(models.Model):
    RentOrSell_CHOICES = [('R','Rent'), ('S','Sell')]
    CondoOrHouse_CHOICES = [('A','Apartment'), ('H','House')]
    house_type = models.CharField(choices=CondoOrHouse_CHOICES,max_length=1)
    listing_type = models.CharField(choices=RentOrSell_CHOICES,max_length=1)
    province = models.ForeignKey('Province',on_delete=models.CASCADE)
    city = models.ForeignKey('City',on_delete=models.CASCADE)
    square = models.FloatField(verbose_name="Square meter")
    bedroom = models.SmallIntegerField(verbose_name="Bedroom No.")
    bath = models.SmallIntegerField(verbose_name="Bath No.")
    postal = models.CharField(max_length=30,blank=True)
    address = models.CharField(max_length=50)
    parking = models.BooleanField(verbose_name="Has Parking")
    furnished = models.BooleanField(verbose_name="Is Furnished")
    photo = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    create_Date=models.DateField(verbose_name="Create Date",editable=False)#Whatch this might change everyday
    modeified_Date=models.DateField(verbose_name="Modified Date",editable=False)#Whatch this might change everyday
    availability = models.DateField(verbose_name="Availability date")
    price = models.FloatField()
    list_owener = models.ForeignKey('A_User',on_delete=models.CASCADE,verbose_name="Post Owner")
    #


    # Metadata: One of the most useful features of this metadata is to
    # control the default ordering of records returned when you query the model type.
    class Meta:
        ordering = ['-create_Date']

class A_User(models.Model):
    first_name = models.CharField(max_length=128,blank=True)
    last_name = models.CharField(max_length=128,blank=True)
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)
    password = models.CharField(max_length=264)
    phone = models.PositiveIntegerField()
    create_Date=models.DateField(verbose_name="Create Date")
    modeified_Date=models.DateField(verbose_name="Modified Date",editable=False)#Whatch this might change everyday

    def __str__(self):
        return self.username


class Province(models.Model):
    province_name = models.CharField(max_length=50)
    def __str__(self):
        return self.province_name

class City(models.Model):
    name = models.CharField(max_length=50)
    province=models.ForeignKey('Province',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
