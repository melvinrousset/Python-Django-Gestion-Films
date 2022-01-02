from django.db import models
from django.shortcuts import redirect, render
from django.urls import reverse
import os
from django.conf import settings










class Movie_Model(models.Model):
    title = models.CharField(max_length=50,)
    description = models.TextField(max_length=500)
    price = models.FloatField()

    image = models.ImageField(upload_to='static/Movie/images')

    def __str__(self) -> str:
        return self.title

    def check_title(self):
        number_list = ['0','1','2','3','4','5','6','7','8','9']
        for number in number_list:
            if self.title.find(number):
                return False

        return True

    def check_price(self):
        if self.price >= 25.0:
            return False

        elif self.price <= 0.0:
            return False

        return True



        


    def get_absolute_url(self):
        return reverse("Movie:Movie-detail-view", kwargs={"title": self.title})
    



# Create your models here.
