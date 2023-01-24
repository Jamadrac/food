from pay import PayClass

response = PayClass.momopay("50", "EUR", "12345", "760071681", "payermessage")

if response.status_code == 202:
    response_dict = response.json()
    print(json.dumps(response_dict, indent=4))
else:
    print(response)