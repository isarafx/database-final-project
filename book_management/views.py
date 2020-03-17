from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import Author, Book, Publisher
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,Http404
from .models import Publisher,Author,Book
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib import messages
import time

# Create your views here.

def homepage (request):
    auth.logout(request)
    count = 0
    ok = ''
    table = []
    if request.method == "POST":
        switch = request.POST["ok"]
        quanity = request.POST["quanity"]
        if quanity in ['10', '100', '1000']:
            if switch == 'Publisher':
                count = 2
                table = Publisher.objects.all().order_by('id')[:int(quanity)]
            elif switch == 'Book':
                count = 1
                table = Book.objects.all().order_by('id')[:int(quanity)]
            elif switch == 'Author':
                count = 3
                table = Author.objects.all().order_by('id')[:int(quanity)]
        else:
            if switch == 'Publisher':
                count = 2
                table = Publisher.objects.all()
            elif switch == 'Book':
                count = 1
                table = Book.objects.all()
            elif switch == 'Author':
                count = 3
                table = Author.objects.all()

    return render(request,'homepage.html',{'rows':table,'count':count})


def home(request):
    count = 0
    ok = ''
    table = []
    if request.method == "POST":
        switch = request.POST["ok"]
        quanity = request.POST["quanity"]
        if quanity in ['10', '100', '1000']:
            if switch == 'Publisher':
                count = 2
                table = Publisher.objects.all().order_by('id')[:int(quanity)]
            elif switch == 'Book':
                count = 1
                table = Book.objects.all().order_by('id')[:int(quanity)]
            elif switch == 'Author':
                count = 3
                table = Author.objects.all().order_by('id')[:int(quanity)]
        else:
            if switch == 'Publisher':
                count = 2
                table = Publisher.objects.all()
            elif switch == 'Book':
                count = 1
                table = Book.objects.all()
            elif switch == 'Author':
                count = 3
                table = Author.objects.all()

    return render(request,'home.html',{'rows':table,'count':count})

def show_book(request):
    all_books = Book.objects.order_by('id')
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    context = {
        'all_books' : all_books,
        'authors' : authors,
        'publishers' : publishers
    }
    return render(request, 'home.html', context)

def insert_book(request):
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    context = {
        'authors' : authors,
        'publishers' : publishers
    }
    if request.method == 'POST':
        book_name = str(request.POST['book_name'])
        publisher = str(request.POST['publisher'])
        pub_date = str(request.POST['publisher_date'])
        author = int(request.POST['author'])
        insert_book = Book(name = book_name, publish_date = pub_date, author_id = author, publisher_id = publisher)
        insert_book.save()
        messages.success(request, 'Your insert successfully.')
    return render(request, 'insert_book.html', context)

def insert_author(request):
    publishers = Publisher.objects.all()
    context = {
        'publishers' : publishers
    }
    if request.method == 'POST':
        author_name = str(request.POST['author_name'])
        address = str(request.POST['address'])
        sex = str(request.POST['sex'])
        tel = str(request.POST['tel'])
        member_in = int(request.POST['publisher'])
        insert_author = Author(name = author_name, address = address, sex = sex, tel = tel, member_in_id = member_in)
        insert_author.save()
        messages.success(request, 'Your insert successfully.')
    return render(request, 'insert_author.html', context)

def insert_publisher(request):
    if request.method == 'POST':
        publisher_name = str(request.POST['pub_name'])
        address = str(request.POST['address'])
        country = str(request.POST['pub_country'])
        insert_publisher = Publisher(name = publisher_name, address = address, country = country)
        insert_publisher.save()
        messages.success(request, 'Your insert successfully.')
    return render(request, 'insert_publisher.html')

def update_book(request):
    all_books = Book.objects.order_by('id')
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    context = {
        'all_books' : all_books,
        'authors' : authors,
        'publishers' : publishers
    }
    if request.method == 'POST':
        book_id = int(request.POST['id'])
        book_name = str(request.POST['book_name'])
        publisher = int(request.POST['pub_id'])
        pub_date = str(request.POST['pub_date'])
        author = int(request.POST['author_id'])
        update_book = Book(id = book_id, name = book_name, publish_date = pub_date, author_id = author, publisher_id = publisher)
        update_book.save()
        messages.success(request, 'Your update successfully.')
    return render(request, 'update_book.html', context)

def update_author(request):
    authors = Author.objects.all()
    context = {
        'authors' : authors,
    }
    if request.method == 'POST':
        author_id = str(request.POST['id'])
        author_name = str(request.POST['author_name'])
        address = str(request.POST['address'])
        sex = str(request.POST['sex'])
        tel = str(request.POST['tel'])
        member_in = int(request.POST['pub_id'])
        insert_author = Author(id = int(author_id), name = author_name, address = address, sex = sex, tel = tel, member_in_id = member_in)
        insert_author.save()
        messages.success(request, 'Your update successfully.')
    return render(request, 'update_author.html', context)

def update_publisher(request):
    publishers = Publisher.objects.all()
    context = {
        'publishers' : publishers
    }
    if request.method == 'POST':
        publisher_id = str(request.POST['id'])
        publisher_name = str(request.POST['pub_name'])
        address = str(request.POST['address'])
        country = str(request.POST['pub_country'])
        insert_publisher = Publisher(id = publisher_id, name = publisher_name, address = address, country = country)
        insert_publisher.save()
        messages.success(request, 'Your update successfully.')
    return render(request, 'update_publisher.html', context)

def delete_book(request):
    all_books = Book.objects.order_by('id')
    context = {
        'all_books' : all_books,
    }
    if request.method == 'POST':
        book_id = int(request.POST['id'])
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
    return render(request, 'delete_book.html', context)

def delete_author(request):
    authors = Author.objects.all()
    context = {
        'authors' : authors,
    }
    if request.method == 'POST':
        author_id = int(request.POST['id'])
        author = get_object_or_404(Author, pk=author_id)
        author.delete()
    return render(request, 'delete_author.html', context)

def delete_publisher(request):
    publishers = Publisher.objects.all()
    context = {
        'publishers' : publishers
    }
    if request.method == 'POST':
        pub_id = int(request.POST['id'])
        pub = get_object_or_404(Publisher, pk=pub_id)
        pub.delete()
    return render(request, 'delete_publisher.html', context)

def dbtable(request):
    count = 0
    ok = ''
    table = []
    if request.method == "POST":
        switch = request.POST["ok"]
        quanity = request.POST["quanity"]
        if quanity in ['10', '100', '1000']:
            if switch == 'Publisher':
                count = 2
                table = Publisher.objects.all().order_by('id')[:int(quanity)]
            elif switch == 'Book':
                count = 1
                table = Book.objects.all().order_by('id')[:int(quanity)]
            elif switch == 'Author':
                count = 3
                table = Author.objects.all().order_by('id')[:int(quanity)]
        else:
            if switch == 'Publisher':
                count = 2
                table = Publisher.objects.all()
            elif switch == 'Book':
                count = 1
                table = Book.objects.all()
            elif switch == 'Author':
                count = 3
                table = Author.objects.all()
    return render(request,'dbtable.html',{'rows':table,'count':count})

def signup (request):
    return render(request,'signup.html')

def createuser (request):
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    username = request.POST.get("username")
    password = request.POST.get("password")
    rpassword = request.POST.get("rpassword")
    email1 = request.POST.get("email1")

    if password == rpassword:
        if User.objects.filter(username=username).exists():
            # print("UserName already used")
            messages.info(request,"UserName already used")
            return redirect('/signup')
        elif User.objects.filter(email=email1).exists():
            # print("Email already used")
            messages.info(request,"Email already used")
            return redirect('/signup')
        else:
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email1,
                first_name = firstname,
                last_name = lastname
            )
            user.save()
            return render(request,'createuser.html')
    else :
        # print("Password not match")
        messages.info(request,"Password not match")
        return redirect('/signup')

def phichet (request):
    return render(request,'phichet.html')





