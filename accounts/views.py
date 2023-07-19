from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import ProductForm, CreateUserForm, EditCompany
from . filters import ProductsFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users


def home(request):

    products = Products.objects.all()
    context = {'company':company, 'products':products}

    return render(request, 'accounts/home.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Company.objects.create(
                user=user,
            )
            group = Group.objects.get(name='company')
            user.groups.add(group)


            messages.success(request, 'Accounted created for ' + username)

            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register_page.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['company', 'admin'])
def company_form(request, pk):
    company = Company.objects.get(id=pk)
    
    formset = EditCompany(instance=company)
    if request.method == 'POST':
        formset = EditCompany(request.POST, request.FILES, instance=company)
        if formset.is_valid():
            formset.save()

            return redirect('home')

    context = {'formset':formset, 'company':company}
    return render(request, 'accounts/company_form.html', context)

def company_guest(request, pk):
    company = Company.objects.get(id=pk)

    products = company.products_set.all()
    context = {'company':company, 'products':products}
    return render(request,'accounts/company_guest.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['company', 'admin'])
def company(request, pk):
    pk = request.user.company.id
    company = Company.objects.get(id=pk)

    products = company.products_set.all()
    context = {'company':company, 'products':products}
    return render(request,'accounts/company.html', context)


def catalogue(request):
    catalogue = Products.objects.all()
    productsFilter = ProductsFilter(request.GET, queryset=catalogue)
    #products = ProductsFilter.qs
    catalogue = productsFilter.qs

    context = {'catalogue':catalogue, 'productsFilter':productsFilter}

    return render(request, 'accounts/catalogue.html', context)


def comp_catalogue(request):
    company = Company.objects.all()
    context = {'company':company}

    return render(request, 'accounts/comp_catalogue.html', context)

def products(request, pk):
    products = Products.objects.get(id=pk)
    context = {'products':products}
    return render(request,'accounts/products.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['company', 'admin'])
def create_products(request, pk):
    ProductFormSet = inlineformset_factory(Company, Products, fields=('name', 'image', 'price', 'category', 'tags', 'description'), extra=4)
    company = Company.objects.get(id=pk)
    formset = ProductFormSet(queryset=Products.objects.none(), instance=company)
    #form = ProductForm(initial={'company':company})
    if request.method == 'POST':
        formset = ProductFormSet(request.POST, request.FILES, instance=company)
        #form = ProductForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/catalogue')

    context = {'formset':formset, 'company':company}
    return render(request, 'accounts/product_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['company', 'admin'])
def update_product(request, pk):
    products = Products.objects.get(id=pk)
    formset = ProductForm(instance=products)
    
    if request.method == 'POST':

        formset = ProductForm(request.POST, instance=products)
        if formset.is_valid():
            formset.save()
            return redirect('/catalogue')

    context = {'formset':formset, 'products':products}
    return render(request, 'accounts/product_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['company', 'admin'])
def delete_product(request, pk):
    products = Products.objects.get(id=pk)
    if request.method == 'POST':
        products.delete()
        return redirect('/catalogue')

    context = {'products':products}
    return render(request, 'accounts/delete_product.html', context)


def contacts_page(request):

    return render(request, 'accounts/contacts.html',)
