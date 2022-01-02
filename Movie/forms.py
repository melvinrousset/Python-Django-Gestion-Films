from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.shortcuts import redirect, render
from .models import Movie_Model
import os
from django.conf import settings



class Movie_Model_Forms(forms.ModelForm):
    class Meta:
        model = Movie_Model
        fields=[
            'title',
            'description',
            'price',
            'image'
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        queryset = Movie_Model.objects.all()
        for movie in queryset:
            if title == movie.title:
                raise forms.ValidationError("this Movie already exist ! ")
        return title

    def updateimage(request, id):  #this function is called when update data
        old_image = Movie_Model.objects.get(id=id)
        form = Movie_Model_Forms(request.POST, request.FILES, instance=old_image)

        if form.is_valid():

        # deleting old uploaded image.
            image_path = old_image.image_document.path
            if os.path.exists(image_path):
                os.remove(image_path)

        # the `form.save` will also update your newest image & path.
            form.save()
            return redirect("/Movie/")
        else:
            context = {'singleimagedata': old_image, 'form': form}
            return render(request, 'Movie/Update_Movie.html', context)

