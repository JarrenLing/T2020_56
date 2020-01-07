import json
import requests

api_headers = {'identity': 'T28', 'token': '8a30bcbf-72f0-4a7a-8156-eaf4d554a330'}


def api_getUserID(username):
    api_url = 'http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/customers/' + username
    response = requests.get(api_url, headers=api_headers)
##    {
##    "userName": "marytan",
##    "customerId": "2"
##    }
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data["customerId"]
    else:
        return None


def api_getCustomerDetails(customerId):
    api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/customers/{customerId}/details"
    response = requests.get(api_url, headers=api_headers)
##     {
##         "customerId": "2",
##         "gender": "Female",
##         "firstName": "Hui Shan",
##         "lastName": "Tan",
##         "lastLogIn": "2019-01-29T18:00:00.000+0000",
##         "dateOfBirth": "1992-03-25T00:00:00.000+0000"
##         "riskLevel": "High"
##     }
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        return None

def api_getTransactionDetails(accountId):
    api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/transactions/{accountId}?from=01-01-2018&to=01-30-2020"
    response = requests.get(api_url, headers=api_headers)
##    [
##      {
##        "transactionId": "58214df1-0635-4a47-b963-dd08343cb050",
##        "accountId": 79,
##        "type": "DEBIT",
##        "amount": "16.58",
##        "date": "2018-01-01T17:00:00.000+0000",
##        "tag": "TRANSFER",
##        "referenceNumber": "818385318 BANK FAST TRANSFER TO 975325540"
##      },
##    ]
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        print("this is the error")
        print(response.status_code)
        return None


def api_getListOfDepositAccounts(customerId):
    api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{customerId}"
    response = requests.get(api_url, headers=api_headers)
    # [
    #     {
    #         "accountId": 79,
    #         "type": "SAVINGS",
    #         "displayName": "POSB SAVINGS ACCOUNT",
    #         "accountNumber": "490723483"
    #     }
    # ]
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        return None




#3.4 GET Details of a Marketing Message

api_headers = {'identity': 'T28', 'token': '8a30bcbf-72f0-4a7a-8156-eaf4d554a330'}


def api_getmarketingmsgs():
    api_url = 'http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/marketing/'
    response = requests.get(api_url, headers=api_headers)
#     [
#     {
#         "messageId": 1,
#         "dateCreated": "2018-12-20T08:00:00.000+0000",
#         "summary": "Grab discount with PayLah!",
#         "type": "Savings"
#     },
#     {
#         "messageId": 2,
#         "dateCreated": "2018-12-20T08:06:40.000+0000",
#         "summary": "GoJek voucher with DBS card",
#         "type": "Savings"
#     },
#     {
#         "messageId": 3,
#         "dateCreated": "2018-12-20T08:26:40.000+0000",
#         "summary": "Cashback with DBS new credit card",
#         "type": "Credit Cards"
#     }
# ]
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        return None

#print(api_getmarketingmsgs('2')) #hardcoded to marytan first


# 3.5 GET Personal Messages

def api_getpersonalmsgs(customerid): #standardize to 2 for now - remove for dynamism later
    api_url = 'http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/message/' + customerid
    response = requests.get(api_url, headers=api_headers)

# [
#     {
#         "messageId": 20001,
#         "dateCreated": "2019-01-26T07:15:00.000+0000",
#         "topic": "Credit Cards",
#         "subject": "Cancel Card",
#         "body": "Hi, I would like to cancel my cc XXXX-XXXX-XXXX-3123. Thanks, Hui Shan.",
#         "isRead": true
#     },
#     {
#         "messageId": 20003,
#         "dateCreated": "2019-01-30T01:12:00.000+0000",
#         "topic": "Credit Cards",
#         "subject": "Cancel Card",
#         "body": "Dear Ms Tan, your credit card ending with 3123 has successfully been cancelled.",
#         "isRead": false
#     }
# ]

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data['summary']
        print(data)
    else:
        return None

#print(api_getpersonalmsgs('2')) #hardcoded to marytan first



def  api_getAccountBalance(accountId):
	# should we add the month and year in the url?
    api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{accountId}/balance?month=0&year=2020"
    response = requests.get(api_url, headers=api_headers)
# {
#     "availableBalance": "11014.92",
#     "currency": "SGD",
#     "dateOfBalance": "2018-02-28T08:00:00.420+0000",
#     "displayName": "POSB SAVINGS ACCOUNT",
#     "accountNumber": "143497293",
#     "accountType": "SAVINGS"
# }
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        return None















