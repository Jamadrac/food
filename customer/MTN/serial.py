from pay import PayClass

callpay = PayClass.momopay("50", "EUR", "10101", "0760071681", "food purchase")
print(callpay["response"])
