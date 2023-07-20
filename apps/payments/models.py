from django.db import models
from apps.common.models import BaseModel


class PurposePayment(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Payment(BaseModel):
    full_name = models.CharField(max_length=64)
    amount = models.IntegerField()
    purpose_payment = models.ForeignKey("payments.PurposePayment", on_delete=models.SET_NULL, related_name="payment")
    doc_file = models.FileField(upload_to="apps/payments/doc_files", null=True, blank=True)

    def __str__(self):
        return self.full_name
