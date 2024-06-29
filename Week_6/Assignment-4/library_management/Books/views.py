from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView
from users.models import UserBankAccount
from .forms import ReviewForm
from .models import BookModel,Borrow
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from users.views import send_mail
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import BookModel, Review

def ReviewViewFunc(request,id):
    book =get_object_or_404(BookModel,pk=id)
    if request.method=='POST':
        form=ReviewForm(request,request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            # print('hello')
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
def BorrowBookView(request, id):
    book = get_object_or_404(BookModel, pk=id)
    requested_user = UserBankAccount.objects.get(user=request.user)

    try:
        borrow = Borrow.objects.get(pk=id)
    except Borrow.DoesNotExist:
        borrow = None

    if borrow is None:
        if requested_user.balance >= book.price:
            requested_user.balance -= book.price
            requested_user.save()
            Borrow.objects.create(user=request.user, book=book)
            messages.success(request, 'You successfully borrowed this book.')
            return redirect('home')
        else:
            messages.error(request, 'You cannot borrow this book because your balance is less than the book price.')
    else:
        messages.error(request, 'This book is already borrowed.')

    return redirect('home')


@login_required
def ReturnBook(request, id):
    book = get_object_or_404(BookModel, pk=id)
    
    borrow_instances = Borrow.objects.filter(book=book, user=request.user, return_date=None)

    if borrow_instances.exists():
        user_account = request.user.account
        total_balance_to_add = 0

        for borrow_instance in borrow_instances:
            total_balance_to_add += borrow_instance.book.price

        user_account.balance += total_balance_to_add
        user_account.save(update_fields=['balance'])

        borrow_instances.update(return_date=datetime.now())
        borrow_instances.delete()  

    return redirect('home')  


class BorrowedBookView(LoginRequiredMixin,ListView):
    template_name='./Books/profile.html'
    model=Borrow
    context_object_name='borrowed_books'
    def get_queryset(self):
         queryset=super().get_queryset().filter(user=self.request.user)
         return queryset
    

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = './Books/profile.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        borrowed_books = Borrow.objects.filter(user=self.request.user, return_date=None)
    
        context['borrowed_books'] = borrowed_books
        return context
    
@login_required
def submit_review(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(BookModel, id=book_id)
        review_body = request.POST['review_body']
        rating = request.POST['rating']
        
        Review.objects.create(
            book=book,
            user=request.user,
            body=review_body,
            rating=rating
        )
        
        messages.success(request, 'Review submitted successfully!!!')
        return redirect('profile') 

    return redirect('book_detail', book_id=book_id)   