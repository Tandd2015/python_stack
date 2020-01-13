from django.shortcuts import render, redirect
from .models import Order, Product, User

def index(request):
    if 'logged_user' not in request.session:
        new = User.objects.last()
        request.session['logged_user']= new.id
    else:
        request.session['logged_user'] = request.session['logged_user']
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout_index(request):
    new_total_money_spent = 0
    in_new_order= Order.objects.last()
    new_total_order_count= Order.objects.filter(user_id=in_new_order.user_id)
    for orderzzz in new_total_order_count:
        new_total_money_spent += (orderzzz.product.price * orderzzz.quantity_ordered)
    context ={
        'new_order': in_new_order,
        'total_order': len(new_total_order_count),
        'total_money': new_total_money_spent,
    }
    return render(request, "store/checkout.html", context)
    
def amadon_buying(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    add_product = Product.objects.get(price=price_from_form)
    add_user = User.objects.get(id=request.session['logged_user'])
    new = Order.objects.create(quantity_ordered=quantity_from_form, order_total_price=total_charge, user_id=add_user, product=add_product)
    return redirect('/checkout')

