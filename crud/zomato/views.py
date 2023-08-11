from django.shortcuts import render,HttpResponse

# Create your views here.


menu_data = [
    {'dish_id': 1, 'dish_name': 'Margherita Pizza', 'price': 10.99, 'availability': True},
    {'dish_id': 2, 'dish_name': 'Pasta Carbonara', 'price': 8.99, 'availability': True},
    {'dish_id': 3, 'dish_name': 'Chicken Tandoori', 'price': 12.99, 'availability': False},
    # Add more sample dishes here
]
# views.py

order_data = []


def menu_view(request):
    return render(request, 'menu.html', {'menu_data': menu_data})

def add_dish_view(request):
    if request.method == 'POST':
       
        new_dish = {
            'dish_id': len(menu_data) + 1,  # Assign a unique dish ID
            'dish_name': request.POST['dish_name'],
            'price': float(request.POST['price']),
            'availability': True if request.POST.get('availability') == 'on' else False,
        }
        menu_data.append(new_dish)
        # return redirect('menu')  # Redirect to the menu view after adding the dish

    return render(request, 'add.html')




def remove(request):
    if request.method == 'POST':
        # Retrieve the dish_id from the request's POST parameters
        dish_id = request.POST.get('dish_id')
        
        # Assuming menu_data is a list of dictionaries containing dish information
        menu_data[:] = [dish for dish in menu_data if dish['dish_id'] != int(dish_id)]
        
        context = {
            'dish_id': dish_id,
        }
        
        return render(request, 'remove.html', context)
    else:
        return HttpResponse("Invalid request method.")








def update(request):
    if request.method == 'POST':
       
        dish_id = request.POST.get('dish_id')
        
      
        dish = next((d for d in menu_data if d['dish_id'] == int(dish_id)), None)
        
        if dish:
            dish['dish_name'] = request.POST['dish_name']
            dish['price'] = float(request.POST['price'])
            dish['availability'] = request.POST.get('availability') == 'on'

            context = {
                'dish_id': dish_id,
                'dish': dish,  # Keep the 'dish' in context
                # other context variables
            }
            
            return render(request, 'update.html', context)
        else:
            return HttpResponse("Dish not found.")
    else:
        return HttpResponse("Invalid request method.")



# views.py

def take_order(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        dish_ids = [int(d_id) for d_id in request.POST['dish_ids'].split(',') if d_id.strip()]
        
        new_order = {
            'order_id': len(order_data) + 1,
            'customer_name': customer_name,
            'dish_ids': dish_ids,
            'status': 'received'
        }
        order_data.append(new_order)
        
    return render(request, 'order.html')

# views.py

# views.py

def review_orders(request):
    context = {'order_data': order_data}
    return render(request, 'review.html', context)



# views.py

def update_order_status(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        new_status = request.POST.get('status')
        
        order = next((o for o in order_data if o['order_id'] == int(order_id)), None)
        
        if order:
            valid_statuses = ['received', 'preparing', 'ready for pickup', 'delivered']
            if new_status in valid_statuses:
                order['status'] = new_status
        
        context = {
            'order_id': order_id,
            'order': order,
        }
        
        return render(request, 'updated_review.html', context)
    
    return HttpResponse("Invalid request method.")


def exit_option(request):
    # You can perform any necessary cleanup or actions here before exiting
    # For example, saving data to a database, logging out users, etc.
    return render(request, 'exit.html')
