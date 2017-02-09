from django import template
from fruitclub.models import Product, Cart

register = template.Library()

@register.simple_tag(takes_context=True)
def cart_count(context):
	request = context['request']
	count = 0
	if request.user.is_authenticated():
		count = Cart.objects.filter(user=request.user).count()
	return count

@register.simple_tag(takes_context=True)
def cart_amount(context):
	request = context['request']
	amount = 0
	if request.user.is_authenticated():
		cart = Cart.objects.filter(user=request.user)
		for product in cart:
			amount += product.product.price * product.quantity
	return amount