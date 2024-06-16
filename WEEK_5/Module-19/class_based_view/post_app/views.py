from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView 



@login_required
def add_post(request):
    if request.method == 'POST':
        post_form  = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.PostForm()    
    return render(request, './post_app/add_post.html', {'form' : post_form})


# add post using class based view
@method_decorator(login_required, name='dispatch')
class addPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = './post_app/add_post.html'  
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author =  self.request.user
        return super().form_valid(form)


@login_required
def edit_post(request, id):  
    post = models.Post.objects.get(pk = id)
    post_form  = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form  = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author =  request.user
            post_form.save()
            return redirect('home')
    return render(request, './post_app/add_post.html', {'form' : post_form})


# edit post using class based view
class editPostUpdateView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = './post_app/add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')      

# delete post using class based view
class deletePostView(DeleteView):
    model = models.Post
    template_name = './post_app/delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


class DetailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = './post_app/post_details.html'