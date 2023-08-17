import requests
import json
from pprint import pprint
import os
from dotenv import load_dotenv
import random

load_dotenv()


eCheck = {
     "bankAccount": {
                    "accountType": random.choice(["checking","savings","businessChecking"]),
                    "routingNumber": "031101279",
                    "accountNumber": "18961896",
                    "echeckType":random.choice(["ARC","BOC", "CCD", "PPD", "TEL","WEB"]),
                    "nameOnAccount": "Charles Dickens",
                    "checkNumber": str(random.randint(100_000,100_000_000_000_000))
                    }
}

for x in range(2):

    payload = {
        "createTransactionRequest": {
            "merchantAuthentication": {
                "name": os.getenv("API_LOGIN_ID"),
                "transactionKey": os.getenv("API_TRANS_KEY")
            },
            "refId": "123456",
            "transactionRequest": {
                "transactionType": "authCaptureTransaction",
                "amount": random.choice(['5.00','10.00','15.00','20.00','30.00']),
                "payment": {
                    "creditCard": {
                        "cardNumber": random.choice(["5424000000000015","3088000000000017" , "370000000000002", "6011000000000012", "4012888818888", "2223000010309711"]),
                        "expirationDate": "2025-12",
                        "cardCode": str(random.randint(100,999))
                    }
    }
            }
        }
    }


    # payload_two = {
    #     "getHostedPaymentPageRequest": {
    #         'name': os.getenv("API_LOGIN_ID"),
    #         "transactionKey": os.getenv("API_TRANS_KEY")
    #     },
    #     'transactionRequest':{
    #         'transactionType':'authCaptureTransaction',
    #         'amount': random.choice(["5424000000000015", "370000000000002", "6011000000000012", "4012888818888", "2223000010309711"]),
    #     }
    # }
    pay_req = json.dumps(payload)

    result = requests.post(os.getenv("PROD_ENDPOINT"), pay_req)
    pprint(result.text)

# print(requests.get(endpoint))
