from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fruitclub.models import Profile, SlideShowImage, ImageGroup, Product, Cart, Category
from fruitclub.forms import ProfileForm
from django.http import HttpResponse
from instamojo_wrapper import Instamojo

# Create your views here.
api = Instamojo(api_key='e592148daf8eae546e01e6b2f18ad1fb',
                auth_token='9e09a975978993c860602dcef3ec76f3')



def index(request):
	product_list = Product.objects.all()
	slideshow = ImageGroup.objects.get(name='banner')
	image_list = SlideShowImage.objects.filter(slideshow=slideshow)
	context_dict = {'image_list':image_list, 'product_list':product_list}
	return render(request, 'fruitclub/index.html', context_dict)

@login_required
def profile(request):
	if request.method == 'POST':
		profileform = ProfileForm(request.POST)
		if profileform.is_valid():
			profile = profileform.save(commit=False)
			profile.user = request.user
			profile.save()
		return redirect(index)
	else:
		profileform = ProfileForm()
	return render(request, 'fruitclub/profile.html', {'profileform':profileform})

def profile_page(request):
	profile = Profile.objects.get(user=request.user)
	return render(request, 'fruitclub/profile_page.html', {'profile':profile})

@login_required
def add_cart(request):
	pid = request.POST['pid']
	quantity = request.POST['quantity']
	product = Product.objects.get(id=pid)
	if product:
		try:
			entry = Cart.objects.get(user=request.user, product=product)
		except Cart.DoesNotExist:
			entry = None
		if entry:
			if entry.quantity != quantity:
				entry.quantity = quantity
				entry.save()
		else:
			Cart.objects.create(user=request.user, product=product, quantity=quantity)
		return HttpResponse()

def single_product(request, product_slug):
	product = Product.objects.get(slug=product_slug)
	context_dict = {'product':product}
	return render(request, 'fruitclub/single_product.html', context_dict)

def cart(request):
	product_list = Cart.objects.filter(user=request.user)
	context_dict = {'product_list':product_list}
	return render(request, 'fruitclub/cart.html', context_dict)

def remove_item(request):
	pid = request.GET['pid']
	product = Product.objects.get(id=pid)
	Cart.objects.get(user=request.user, product=product).delete()
	return HttpResponse()

def change_qty(request):
	pid = request.GET['pid']
	qty = request.GET['qty']
	prod = Cart.objects.get(user=request.user, product=Product.objects.get(id=pid))
	prod.quantity = qty
	prod.save()
	return HttpResponse()

def about(request):
	return render(request, 'fruitclub/about.html')

def category(request, category_slug):
	category = Category.objects.get(slug=category_slug)
	product_list = Product.objects.filter(category=category)
	return render(request, 'fruitclub/category.html', {'product_list':product_list, 'category':category})

@login_required
def checkout(request):
	cart_list = Cart.objects.filter(user=request.user)
	amount = 0
	for product in cart_list:
		amount += product.product.price * product.quantity
	response = api.payment_request_create(
			amount=amount,
			buyer_name=request.user.profile.first_name,
			purpose="purchase from fruitclub",
			send_email=False,
			email=request.user.email,
			redirect_url="https://nextamazon.herokuapp.com",
			phone=request.user.profile.mobile
		)
	url = response['payment_request']['longurl']
	context_dict = {'url':url, "amount":amount}
	return render(request, 'fruitclub/checkout.html', context_dict)
