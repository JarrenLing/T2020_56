# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, session, request

import webapi

# create the application object
app = Flask(__name__, static_url_path='/static')

# create username and password ## edit
users = {
'limzeyang': 'password1',
'marytan': 'password2',
'ahmadfarhan': 'password3'
}

# use decorators to link the function to a url
@app.route('/', methods=["GET", "POST"])
# Route for handling the login page logic
## login page
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		
		username = request.form['username']
		password = request.form['password']

		if username in users.keys() and password == users.get(username):
			session['logged_in'] = True
			session['username'] = username
			
			if username == 'limzeyang':
				session["accountid"] = 10
				session['userid'] = 1
			elif username == "marytan":
				session["accountid"] = 79
				session['userid'] = 2
			elif username == "ahmadfarhan":
				session["accountid"] = 94
				session['userid'] = 3

			return redirect(url_for('dashboard'))


		else:
			error = 'Invalid Credentials. Please try again.'

	return render_template('login.html', error=error)  

@app.route('/dashboard')
def dashboard():
	if 'username' in session: ## do not change the 'username'
		# labels, data = useCarparkData()
		bank_balance = BankBalance(session["accountid"])
		user_id = getUserID(session['username'])
		customer_details = getCustomerDetails(session['userid'])
		list_of_dep_acc = getListOfDepositAccounts(session['userid'])
		marketingmsgs = getmarketingmsgs('1')
		acc_balance = getAccountBalance(session['accountid'])



		return render_template('dashboard.html', bank_balance=bank_balance, user_id=user_id, customer_details=customer_details, list_of_dep_acc=list_of_dep_acc, marketingmsgs=marketingmsgs, acc_balance=acc_balance)  # render a template
	else: 
		return 'You are not logged in'

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/transaction')
def transaction():

	transaction_details = getTransactionDetails(session['accountid'])

	return render_template('transaction.html', transaction_details=transaction_details)  


@app.route('/personal')
def personal():

	personalmsgs = getpersonalmsgs(session['userid'])

	return render_template('personal.html', personalmsgs=personalmsgs) 


@app.route('/transfer')
def transfer():

	return render_template('transfer.html') 


@app.route('/others')
def others():

	return render_template('others.html') 


# def useCarparkData():
# 	details = webapi.getCarparkAvailability('2019-12-31T09:54:15')
# 	top10 = details['items'][0]['carpark_data']
# 	labels, data = [], []
# 	for each in top10: 
# 		labels.append(each['carpark_number'])
# 		data.append(int(each['carpark_info'][0]['total_lots']))
# 	labels, data = labels[:10], data[:10]
# 	return labels, data

#=================== FUNCTIONS=============================================


def BankBalance(accountid):

    bank_balance = webapi.api_getAccountBalance(accountid)

    return bank_balance

def getUserID(username):
	user_id = webapi.api_getUserID(username)

	return user_id

def getCustomerDetails(userid):
	customer_details = webapi.api_getCustomerDetails(userid)

	return customer_details

def getTransactionDetails(accountid):
	transaction_details = webapi.api_getTransactionDetails(accountid)

	return transaction_details

def getListOfDepositAccounts(userid):
	list_of_dep_acc = webapi.api_getListOfDepositAccounts(userid)

	return list_of_dep_acc

def getmarketingmsgs(msgid):
	marketingmsgs = webapi.api_getmarketingmsgs(msgid)

	return marketingmsgs


def getpersonalmsgs(userid):
	personalmsgs = webapi.api_getpersonalmsgs(userid)

	return personalmsgs

def getAccountBalance(accountid):
	acc_balance = webapi.api_getAccountBalance(accountid)

	return acc_balance


# def getUserID():
# 	user_details = webapi.api_getUserID()
# 	username, customerid = [], []




# def expenditure():
#     transaction_details = webapi.api_getTransactionDetails()
#     exp = {}

#     for i in transaction_details:
#         if i["tag"] not in exp:
#             exp[i["tag"]] = 1
#         else:
#             exp[i["tag"]] += 1

#     return exp


# start the server with the 'run()' method
if __name__ == '__main__':
	app.secret_key = 'secret123'
	app.run(debug=True)