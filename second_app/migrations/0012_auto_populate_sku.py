from django.db import migrations

def assign_sku(apps, schema_editor):
    # Get the product model
    product = apps.get_model('second_app', 'product')
    
    # Get all existing products that still have TEMP-SKU
    products_to_update = product.objects.filter(sku='TEMP-SKU')
    
    # Assign unique SKU to each
    for index, item in enumerate(products_to_update, start=1):
        item.sku = f"PRD-{index:04d}"  # Creates PRD-0001, PRD-0002, etc.
        item.save()

def reverse_sku(apps, schema_editor):
    # Optional: What to do if migration is rolled back
    product = apps.get_model('second_app', 'product')
    product.objects.all().update(sku='TEMP-SKU')

class Migration(migrations.Migration):
    dependencies = [
        ('second_app', '0011_product_sku'),  # ← Use YOUR actual migration number
    ]

    operations = [
        migrations.RunPython(assign_sku, reverse_sku),
    ]
