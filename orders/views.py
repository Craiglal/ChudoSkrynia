from django.shortcuts import render, get_object_or_404
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import OrderCreated
from .models import OrderProduct


def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderProduct.objects.create(order=order, product=item['product'], price=item['price'],
                                            quantity=item['quantity'])
            cart.clear()
            OrderCreated.delay(order.id)
            return render(request, 'order/created.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form})
