from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def OrderCreated(order_id):
    """
    Отправка Email сообщения о создании покупке
    """
    order = Order.objects.get(id=order_id)
    subject = 'Замовлення з номером {}'.format(order.id)
    message = 'Шановний(а), {}, ви успішно зробили замовлення.\
               Номер вашого замовлення {}'.format(order.first_name, order.id)
    mail_send = send_mail(subject, message, 'admin@myshop.ru', [order.email])
    return mail_send
