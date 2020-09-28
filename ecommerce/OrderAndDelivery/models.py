from django.db import models
from User import models as user_models
from helper import modelHelper
from CartSystem import models as cart_models
from django.db.models import Q


class OrderItem(user_models.AbstractTimeStamp):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    item = models.ForeignKey("Products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "Quantity: {} {}, Product: {} - Rs. {}".format(self.quantity, self.item.sizes or '',
                                             self.item.english_name, self.item.price*self.quantity)

class DeliveredManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=3).order_by('created_at')


class Order(user_models.AbstractTimeStamp):
    item = models.ManyToManyField(OrderItem, blank=False)
    user = models.ForeignKey(user_models.User, null=True, blank=True, on_delete=models.PROTECT)
    status = models.IntegerField(choices=modelHelper.order_status_choice, null=False, blank=False, default=1)
    grand_total = models.FloatField(null=True, blank=True)
    vendor = models.ForeignKey("Vendor.vendor", on_delete=models.PROTECT)
    objects = models.Manager()
    delivered_objects = DeliveredManager()

    def __str__(self):
        return self.user.get_full_name()

    def associated_name(self):
        return self.user.get_full_name()


class Delivery(user_models.AbstractTimeStamp):
    order = models.OneToOneField(Order, null=False, blank=False, on_delete=models.PROTECT)
    note = models.TextField(null=False, blank=False)
    location = models.ForeignKey(cart_models.Location, null=False, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.order.user.get_full_name()