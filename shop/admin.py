# shop/admin.py
from django.contrib import admin
from .models import Category, Product, ProductImage, Order, OrderItem, Payment

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category',)
    inlines = [ProductImageInline]
    search_fields = ('name',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'quantity', 'price')
    can_delete = False
    extra = 0

class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_amount', 'payment_method', 'created_at')
    list_filter = ('status', 'payment_method')
    inlines = [OrderItemInline, PaymentInline]
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
