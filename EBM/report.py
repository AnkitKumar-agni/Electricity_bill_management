# import razorpay
# client = razorpay.Client(auth=("rzp_test_nnz8x3lbvjCFOd", "adg0n6IIyh0pWknezwVY1WG6"))
#
# client.set_app_details({"title" : "python", "version" : "3.10.1"})
#
# order1 = client.order.create({
#   "amount": 100,
#   "currency": "INR",
#   "receipt": "receipt#1",
#
# })
#
# print(order1['id'])
# id_order = order1['id']
# print(id_order)
# print(type(id_order))
#
# order_id = client.order.fetch(id_order)
# print(type(order_id))
# print(order_id)


import requests as r



url = "http://localhost:63342/PycharmProjects/EBM/paymentpage/pay.html?_ijt=e06nj21m6fgbgs9tp5bd7mngaa&_ij_reload=RELOAD_ON_SAVE"

response = r.get(url)
print(response.status_code)

print(response.json())
