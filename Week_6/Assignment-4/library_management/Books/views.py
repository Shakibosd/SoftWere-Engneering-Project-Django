from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView
from .models import Review
from .forms import ReviewForm
from .models import BookModel,Borrow
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from users.views import send_mail
from datetime import datetime

def ReviewViewFunc(request,id):
    book =get_object_or_404(BookModel,pk=id)
    if request.method=='POST':
        form=ReviewForm(request,request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            print('hello')
            user=request.user
            f.book=book
            f.user=user 
            f.save()
            messages.success(request,f'your review succesfully submitted')
            return redirect('home')
    else:
        form=ReviewForm()
    return render(request,'./Books/review.html',{'form':form})

class BookDetailsView(DetailView):
    template_name='./Books/book_details.html'
    model=BookModel
    pk_url_kwarg='id'
    success_url=reverse_lazy('home')
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        id=self.kwargs.get('id')
        book=BookModel.objects.get(pk=id)
        context['book']=book
        return context
    
@login_required
def BorrowBookView(request,id):
    balance=request.user.account.balance
    book=BookModel.objects.get(pk=id)
    try:
        borrow=Borrow.objects.get(book=book)
    except:
        borrow=None
    if borrow is None:
      if  balance>=book.price :
         request.user.account.balance-=book.price
         request.user.account.save(
           update_fields=['balance']
       )
         usr=request.user
         Borrow.objects.create(book=book,user=usr)
         send_mail(usr,'Borrowed Book',usr.email,book)
         messages.success(request,f'You successfully borrow This book')
      else:
        messages.success(request,f'you can not buy this book bacause your balance is lessthan book price')
    return redirect('home')

@login_required
def ReturnBook(request,id):
    book=get_object_or_404(BookModel,pk=id)
    borrow_instance=get_object_or_404(Borrow,book=book)
    if borrow_instance.user==request.user:
        usr=request.user
        usr.account.balance+=book.price
        usr.account.save(
            update_fields=['balance']
        )
        borrow_instance.return_date=datetime.now()
        borrow_instance.save(
            update_fields=['return_date']
        )
        borrow_instance.delete()
    
    return redirect('home')

class BorrowedBookView(LoginRequiredMixin,ListView):
    template_name='./Books/borrowed_book_report_history.html'
    model=Borrow
    context_object_name='borrowed_books'
    def get_queryset(self):
         queryset=super().get_queryset().filter(user=self.request.user)
         return queryset
