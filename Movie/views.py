from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from .models import Movie_Model
from .forms import Movie_Model_Forms
import os
from django.conf import settings









class Home_View(View):
    template_name = 'Movie/home.html'
    def get(self,request):
        return render(request,self.template_name)


class Film_List_View(View):
    template_name = 'Movie/List_Movie.html'
    def get(self,request):
        queryset = Movie_Model.objects.all()
        
        context = {}
        context['movie_list'] = queryset
        return render(request,self.template_name,context)

class Film_Detail_View(View):
    template_name = 'Movie/Detail_Movie.html'
    def get(self,request, title=None, *args, **kwargs):
        context = {}
        if title is not None:
            obj = get_object_or_404(Movie_Model, title=title)
            context["object"] = obj
            return render(request,self.template_name,context)

class Film_Update_View(View):
    template_name = 'Movie/Update_Movie.html'
    def get_object(self):

        title = self.kwargs.get('title')
        obj = None
        if title is not None:
            obj = get_object_or_404(Movie_Model,title=title)

        return obj
    def get(self,request,title=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = Movie_Model_Forms(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request,self.template_name,context)

    def post(self,request,title=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = Movie_Model_Forms(request.POST, request.FILES,instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
            return redirect('/Movie/')
        return render(request,self.template_name,context)



class Film_Delete_View(View):
    template_name = 'Movie/Delete_Movie.html'

    def get_object(self):
        title = self.kwargs.get('title')
        obj = None
        if title is not None:
            obj = get_object_or_404(Movie_Model,title=title)
        return obj
    def get(self,request,title=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request,self.template_name,context)

    def post(self,request,title=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/Movie/')
        return render(request,self.template_name,context)

class Film_Create_View(View):
    template_name = 'Movie/Create_Movie.html'
    def get(self,request,*args, **kwargs):
        context ={}
        form = Movie_Model_Forms()
        context['form'] = form
        return render(request,self.template_name,context)


    def post(self,request,*args, **kwargs):
        form = Movie_Model_Forms(request.POST, request.FILES)
        
        if form.is_valid():
        
         
            form.save()

            return redirect('/Movie/Film/')
        context = {'form':form}

        return render(request,self.template_name,context)
            


    

# Create your views here.
