import json
import requests
import time

import webapi

api_headers = {'identity': 'T28', 'token': '8a30bcbf-72f0-4a7a-8156-eaf4d554a330'}


def api_getAccountBalance(accountId = 10):

    #2018 balance

    running_month = 0
    running_year = 2018
    acc_balance = {}
    while running_month <= 3: #separate while loops for 2018 and 2019

        api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{accountId}/balance?month={running_month}&year={running_year}"
        response = requests.get(api_url, headers=api_headers)

        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            balance_date = data['dateOfBalance'][0:7]
            availBalance = data['availableBalance']

            acc_balance[balance_date] = availBalance
        
        elif response.status_code == 429:
            print("Too many api requests?")

        running_month += 1
    
    time.sleep(1)

    while running_month <= 7: #separate while loops for 2018 and 2019

        api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{accountId}/balance?month={running_month}&year={running_year}"
        response = requests.get(api_url, headers=api_headers)

        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            balance_date = data['dateOfBalance'][0:7]
            availBalance = data['availableBalance']

            acc_balance[balance_date] = availBalance
        
        elif response.status_code == 429:
            print("Too many api requests?")

        running_month += 1

    time.sleep(1)

    while running_month <= 11: #separate while loops for 2018 and 2019

        api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{accountId}/balance?month={running_month}&year={running_year}"
        response = requests.get(api_url, headers=api_headers)

        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            balance_date = data['dateOfBalance'][0:7]
            availBalance = data['availableBalance']

            acc_balance[balance_date] = availBalance
        
        elif response.status_code == 429:
            print("Too many api requests?")

        running_month += 1

    #2019 balance
    
    time.sleep(1)

    if running_month == 12:

        running_month = 0
        running_year = 2019
        while running_month <= 3: #because max api calls are 5 per second

            api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{accountId}/balance?month={running_month}&year={running_year}"
            response = requests.get(api_url, headers=api_headers)

            if response.status_code == 200:
                data = json.loads(response.content.decode('utf-8'))
                balance_date = data['dateOfBalance'][0:7]
                availBalance = data['availableBalance']

                acc_balance[balance_date] = availBalance
            
            elif response.status_code == 429:
                print("Too many api requests?")

            running_month += 1

        time.sleep(1) #because max api calls are 5 per second

        while running_month <= 7: 

            api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{accountId}/balance?month={running_month}&year={running_year}"
            response = requests.get(api_url, headers=api_headers)

            if response.status_code == 200:
                data = json.loads(response.content.decode('utf-8'))
                balance_date = data['dateOfBalance'][0:7]
                availBalance = data['availableBalance']

                acc_balance[balance_date] = availBalance
            
            elif response.status_code == 429:
                print("Too many api requests?")

            running_month += 1

        time.sleep(1)

        while running_month <= 11:

            api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{accountId}/balance?month={running_month}&year={running_year}"
            response = requests.get(api_url, headers=api_headers)

            if response.status_code == 200:
                data = json.loads(response.content.decode('utf-8'))
                balance_date = data['dateOfBalance'][0:7]
                availBalance = data['availableBalance']

                acc_balance[balance_date] = availBalance
            
            elif response.status_code == 429:
                print("Too many api requests?")

            running_month += 1

    #2020 balance
    time.sleep(1)

    running_month = 0
    running_year = 2020

    api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{accountId}/balance?month={running_month}&year={running_year}"
    response = requests.get(api_url, headers=api_headers)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        balance_date = data['dateOfBalance'][0:7]
        availBalance = data['availableBalance']

        acc_balance[balance_date] = availBalance
            
    elif response.status_code == 429:
        print("Too many api requests?")


    time.sleep(1) #because max api calls are 5 per second

    return acc_balance
# {
#     "availableBalance": "11014.92",
#     "currency": "SGD",
#     "dateOfBalance": "2018-02-28T08:00:00.420+0000",
#     "displayName": "POSB SAVINGS ACCOUNT",
#     "accountNumber": "143497293",
#     "accountType": "SAVINGS"
# }

def monthly_expenditure_amount(): #monthly expenditure without tags

    transaction_details = webapi.api_getTransactionDetails()
    monthly_amount_exp = {}
    monthly_tag_exp = {}
    for i in transaction_details:
        year_and_month = i['date'][0:7]
        tag = i['tag']
        amount = float(i['amount'])
        type_of_transaction = i['type']
        if type_of_transaction == 'DEBIT':
            if year_and_month not in monthly_amount_exp:
                monthly_amount_exp[year_and_month] = amount
                monthly_tag_exp[year_and_month] = 1
            else:
                monthly_amount_exp[year_and_month] += amount
                monthly_tag_exp[year_and_month] += 1

    return monthly_amount_exp

print(monthly_expenditure_amount())
print(api_getAccountBalance(10)) #took lim ze yang for example
