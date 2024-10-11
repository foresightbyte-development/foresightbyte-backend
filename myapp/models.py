from django.db import models
from accounts.models import *
from django.utils.timezone import now

# Create your models here.



class BaseModel(models.Model):
    """ Abstract base classe some common information """
    # user = models.OneToOneField('accounts.User', verbose_name=_('User'), on_delete=models.CASCADE, null=True, blank=True) # noqa
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-created_at']
        abstract = True



class ChatTitle(BaseModel):
    subadminID = models.ForeignKey(Subadmin, on_delete=models.CASCADE,null=True, blank=True)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    title = models.TextField()



class ChatBody(BaseModel):
    chatTitle_id = models.ForeignKey(ChatTitle, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

 
    


# class ChatTitle(BaseModel):
#     subadminID = models.ForeignKey(Subadmin, on_delete=models.CASCADE,null=True, blank=True)
#     customerID = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
#     unique_id = models.CharField(max_length=5, null=True, blank=True, editable=False)
#     subPrice = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
#     totalPrice = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
#     duePrice = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
#     vat = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
#     vatParcent = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
#     discount = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
#     discountParcent = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
#     transport = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
#     status = models.CharField(max_length=10,  default='pending',null=True)
#     returnTime = models.IntegerField(default=0)

#     def __str__(self) -> str:
#         return str(self.unique_id)