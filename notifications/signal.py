from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from .models import Notification, User
from planning.models import Status

@receiver(post_save, sender=Status)
def send_notification(sender, instance, created, **kwargs):
    if instance.status == Status.MARKETING_FINISHED:
        message = f'The Marketing department has approved work order {instance.work_order_no.id}'
        recipient = User.objects.get(department='PLANNING')
        notification = Notification.objects.create(
            message=message, recipient=recipient)
    elif instance.status == Status.PLANNING_IUSSUE:
        message = f'The Planning department has issued a warning for work order {instance.work_order_no.id}'
        recipient = User.objects.get(department='MARKETING')
        notification = Notification.objects.create(
            message=message, recipient=recipient)
    elif instance.status == Status.PLANNING_REJECTION:
        message = f'The Planning department has rejected work order {instance.work_order_no.id}'
        recipient = User.objects.get(department='MARKETING')
        notification = Notification.objects.create(
            message=message, recipient=recipient)
