from datetime import datetime, timedelta

from django.contrib import admin

from .models import Client, Product, Order, BasketProduct


@admin.action(description="reset phone information")
def update_phone(modeladmin, request, queryset):
    queryset.update(phone='make an e-mail request')


@admin.action(description="change status on active")
def change_status_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="delete object (no active)")
def change_no_active(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="clean all clients (total removal is dangerous!!!)")
def clean_all_table_client(modeladmin, request, queryset):
    clients = Client.all()
    for order in clients:
        order.delete()


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'is_active', 'date_reg']
    ordering = ['name', '-email', 'phone', 'is_active']  # сортировка по очередности в списке
    list_filter = ['name']
    list_per_page = 10
    list_editable = ['email', 'phone', 'address']
    search_fields = ['name', 'email', 'phone', 'address']
    search_help_text = 'customer search by name, email, phone, address'

    actions = [update_phone, change_status_active, change_no_active, clean_all_table_client]

    readonly_fields = ['date_reg']
    fieldsets = [
        (
            'Сustomer information',
            {
                'classes': ['wide'],
                'fields': ['name', 'email'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Address and contact number',
                'fields': ['address', 'phone']
            },
        ),
        (
            'Other',
            {
                'description': 'Additional information',
                'fields': ['date_reg', 'is_active'],
            }
        ),
    ]


@admin.action(description="Reset product quantity to zero")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.action(description="high price with cashback (>1000)")
def filter_with_cashback(modeladmin, request, queryset):
    queryset.filter(price__gte=1000).update(description='price with cashback')


@admin.action(description="mid-range products (100< & <=1000)")
def filter_mid_price(modeladmin, request, queryset):
    queryset.filter(price__lte=100).update(description='average price')


@admin.action(description="low-end products (<100)")
def filter_low_price(modeladmin, request, queryset):
    queryset.filter(price__lte=100).update(description='low price')


@admin.action(description="filter older than 7 days")
def filter_7days(modeladmin, request, queryset):
    how_many_days = 7
    queryset.filter(entered__lte=datetime.now() - timedelta(days=how_many_days)).update(
        description='7 days old')


@admin.action(description="filter older than 30 days")
def filter_30days(modeladmin, request, queryset):
    how_many_days = 30
    queryset.filter(entered__lte=datetime.now() - timedelta(days=how_many_days)).update(
        description='7 days old')


@admin.action(description="complete cleanup of product information (total removal is dangerous!!!)")
def clean_all_table_prod(modeladmin, request, queryset):
    Product.all().delete()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name_product', 'price', 'quantity']
    ordering = ['name_product', 'price', '-date_add']
    list_filter = ['quantity']
    search_fields = ['name_product', 'description']
    search_help_text = 'Search for products by name_product and description'

    actions = [reset_quantity, filter_with_cashback, filter_mid_price, filter_low_price,
               filter_7days, filter_30days, change_status_active, change_no_active, clean_all_table_prod]

    list_per_page = 10
    readonly_fields = ['date_add']
    fieldsets = [
        (
            'Product_name',
            {
                'classes': ['wide'],
                'fields': ['name_product', 'image_product'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'product description and a file with additional information',
                'fields': ['description', 'file_product'],
            },
        ),
        (
            'Accounting',
            {
                'classes': ['collapse'],
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Other',
            {
                'description': 'Additional information',
                'fields': ['date_add', 'is_active'],
            }
        ),
    ]


@admin.action(description="complete cleanup of order information (total removal is dangerous!!!)")
def clean_all_table_order(modeladmin, request, queryset):
    Order.all().delete()


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'date_ordered', 'client_store', 'order_total']
    ordering = ['client_store', '-date_ordered', 'date_change']
    list_filter = ['client_store', 'basket_products']
    search_fields = ['date_ordered', 'order_total']
    search_help_text = 'order search by date_ordered and order_total'

    actions = [change_status_active, change_no_active, clean_all_table_order]
    readonly_fields = ['date_ordered', 'order_total']
    list_per_page = 10
    fieldsets = [
        (
            'Order information',
            {
                'classes': ['wide'],
                'fields': ['client_store'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'shopping cart',
                'fields': ['basket_products'],
            },
        ),
        (
            'Accounting',
            {
                'classes': ['collapse'],
                'fields': ['order_total', 'is_active'],
            }
        ),
        (
            'Other',
            {
                'description': 'Additional information',
                'fields': ['date_ordered'],
            }
        ),
    ]


# admin.site.register(Client)
# admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(BasketProduct)
