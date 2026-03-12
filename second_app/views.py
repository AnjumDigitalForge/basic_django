from django.shortcuts import render, redirect
from . import models
# Create your views here. 

def product_inventory_view(request):
    if request.method == 'POST':
         # Get category_id from form
        category_id = request.POST.get('category_id')
        
        # Get the highest SKU number
        all_products = models.product.objects.all()
        
        if all_products.exists():
            # Extract all SKU numbers and find max
            max_num = 0
            for product in all_products:
                if product.sku and product.sku != 'TEMP-SKU':
                    try:
                        num = int(product.sku.split('-')[1])
                        if num > max_num:
                            max_num = num
                    except (IndexError, ValueError):
                        continue
            new_num = max_num + 1
        else:
            new_num = 1
        
        new_sku = f"PRODUCT ID - {new_num:04d}"

        # if above statement doesn't find any product to change the SKU it will create a new row and will asign new SKU to it.
        models.product.objects.create(
            product_name=request.POST.get('product_name'),
            product_description=request.POST.get('product_description'),
            category_id=category_id,
            product_price=request.POST.get('product_price'),
            product_stock=request.POST.get('product_stock'),
            sku=new_sku,  # ← Auto-assign SKU!
        )
        return redirect('product_list/')
    
    # GET request - show form
    products = models.product.objects.all()
    categories = models.category.objects.all()
    
    return render(request, 'product_inventory.html',{
   'products' : products,
    'categories' : categories
    })

def product_list_view(request):
    products = models.product.objects.all()
    return render(request, 'product_list.html', {
        'products' : products
    })
