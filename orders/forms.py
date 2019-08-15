from django.forms import ModelForm
from django import forms
from .models import Order


class OrderForm(ModelForm):
    OPTIONS = (
        ('',''),
        ('Postpay','Postpay'),
        ('Prepay (Full)','Prepay (Full)'),
        ('Prepay (Half)', 'Prepay (Half)')
    )
    OPTIONS2 = (
        ('Confirm', 'Confirm'),
        ('Ready', 'Ready'),
        ('Send', 'Send'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled')
    )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=OPTIONS)

    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone', 'customer_address', 'creation_date', 'product_id',
                  'payment_option', 'number_of_packets', 'weight', 'inventory_warehouse', 'transportation_vender',
                  'delivery_order_id', 'order_status']
