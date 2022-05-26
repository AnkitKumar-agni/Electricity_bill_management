import razorpay
from django.shortcuts import render, HttpResponse
from paymentpage.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))


def index(request):
    order_amount = 50000
    order_currency = 'INR'
    order_receipt = 'order11'


    payment_order = client.order.create(dict(amount=order_amount, currency=order_currency, payment_capture=1))
    payment_order_id = payment_order['id']

    context = {
        'amount': 500, 'api_key': RAZORPAY_API_KEY, 'order_id': payment_order_id
    }

    return render(request, 'payment.html', context)



