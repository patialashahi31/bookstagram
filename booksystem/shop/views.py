from django.shortcuts import render
from .models import Product, Contact, Orders
from math import ceil
import json
from . import models
import pandas as pd
import numpy as np
# Create your views here.
from django.http import HttpResponse


def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)


def backhome(request):
    return render(request,'shop/backhome.html')


def about(request):
    return render(request, 'shop/about.html')

def loginpage(request):
    return render(request, 'shop/signin.html')


def insert(request):
    y=request.POST['usernamesignup']
    x=request.POST['emailsignup']
    z=request.POST['passwordsignup']
    s= models.detail(username=y,email=x,password=z)
    s.save()
    return HttpResponse("DATA INSERTED ")


def index2(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index2.html', params)


def logincheck(request):

    x=models.detail.objects.all()
    if(request.method=="POST"):
        y=request.POST['username']
        z=request.POST['password']
        for i in x:
            if(i.username==y and i.password==z):
                return render(request,'shop/basic.html',{'username': y})


        return render(request,'shop/error.html')


def knowus(request):
    return render(request, 'shop/knowus.html')



def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def contact2(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact2.html')


def contact3(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact3.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, myid):

    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})

def productView2(request, myid):

    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView2.html', {'product':product[0]})


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')


def books(request):
    books=pd.read_csv('shop/Books.csv' , sep=';',error_bad_lines=False,encoding="latin-1")
    books.columns=['ISBN','bookTitle','bookAuthor','yearOfPublication','publisher','imageUrlS','imageUrlM','imageUrlL']
    users=pd.read_csv('shop/Users.csv',sep=';',error_bad_lines=False,encoding="latin-1")
    users.columns=['userID','Location','Age']
    ratings=pd.read_csv('shop/Ratings.csv',sep=';',error_bad_lines=False,encoding="latin-1")
    ratings.columns=['userId','ISBN','bookRating']
    print(books.shape)
    print (users.shape)
    print(ratings.shape)

    books.drop(['imageUrlS','imageUrlM','imageUrlL'],axis=1,inplace=True)
    books.loc[books.yearOfPublication == 'DK Publishing Inc',:]
    books.loc[books.ISBN == '0789466953','yearOfPublication']=2000
    books.loc[books.ISBN == '0789466953', 'bookAuthor'] = "James Buckley"
    books.loc[books.ISBN == '0789466953', 'publisher'] = "DK Publication Inc"
    books.loc[books.ISBN == '0789466953', 'bookTitle'] = "DK Readers : Creating the X-Men,How Comic Books Come to Life(Level 4:Proeficient reader)"

    books.loc[books.ISBN == '078946697X', 'yearOfPublication'] = 2000
    books.loc[books.ISBN == '0789466953', 'bookAuthor'] = "Michael Teitelbaum"
    books.loc[books.ISBN == '0789466953', 'publisher'] = "DK Publication Inc"
    books.loc[books.ISBN == '0789466953', 'bookTitle'] = "DK Readers : Creating the X-Men,How It all Begin (Level 4:Proeficient reader)"

    books.loc[books.yearOfPublication == 'Gallimard', :]
    books.loc[books.ISBN == '2070426769', 'yearOfPublication'] = 2003
    books.loc[books.ISBN == '2070426769', 'bookAuthor'] = "Jean Marie Gustava Le Cl"
    books.loc[books.ISBN == '2070426769', 'publisher'] = "Gallimard"
    books.loc[books.ISBN == '2070426769', 'bookTitle'] = "Peuple du Ceil, Suivide 'Les Bergers'"

    books.yearOfPublication = books.yearOfPublication.astype(np.int32)
    books.loc[(books.yearOfPublication > 2006)| (books.yearOfPublication==0),'yearOfPublication']= np.NAN
    #books.yearOfPublication.fillna(round(books.yearOfPublication.mean()).inplace=True)
    books.loc[books.publisher.isnull(),:]
    books.loc[(books.ISBN=='193169656X'),'publisher']='other'
    books.loc[(books.ISBN == '1931696993'), 'publisher'] = 'other'

    print(users.shape)
    users.head()
    users.dtypes
    users.userID.values
    print( sorted(users.Age.unique()))
    users.loc[(users.Age > 90 ) | (users.Age <5),'Age']= np.nan
    users.Age=users.Age.fillna(users.Age.mean())
    users.Age=users.Age.astype(np.int32)
    print(sorted(users.Age.unique()))
    ratings.shape
    n_users = users.shape[0]
    n_books = books.shape[0]
    print(n_users * n_books)

    ratings.head(5)
    ratings_new = ratings[ratings.ISBN.isin(books.ISBN)]
    ratings_new = ratings_new[ratings_new.userID.isin(users.userID)]

    sparsity = 1.0 - len(ratings_new) / float(n_users * n_books)

    ratings.bookRating.unique()

    ratings_explicit = ratings_new[ratings_new.bookRating != 0]
    ratings_implicit = ratings_new[ratings_new.bookRating == 0]

    user_exp_ratings = users[users.userID.isin(ratings_explicit.userID)]
    user_imp_ratings = users[users.userID.isin(ratings_implicit.userID)]

    ratings_count = pd.DataFrame(ratings_explicit.groupby(['ISBN'])['bookRating'].sum())
    top10 = ratings_count.sort_values('bookRating', ascending=False).head(10)
    top10.merge(books, left_index=True, right_on='ISBN')
    return render(request,'shop/bd.html',{'books': top10})