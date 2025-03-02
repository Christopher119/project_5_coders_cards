from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """A view to return the shopping cart page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # get existing bag item from session or creating one
    bag = request.session.get('bag', {})

    # incremenet item quantity in bag OR add new item to bag
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    # overwrite bag item in session
    request.session['bag'] = bag
    print(request.session['bag'])

    # redirect back to product detail view
    return redirect(redirect_url)
