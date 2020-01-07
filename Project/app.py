# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, session, request

import webapi

# create the application object
app = Flask(__name__, static_url_path='/static')

# create username and password ## edit
users = {
'user1': 'password1',
'user2': 'password2'
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
			return redirect(url_for('dashboard'))

		else:
			error = 'Invalid Credentials. Please try again.'

	return render_template('login.html', error=error)  

@app.route('/dashboard')
def dashboard():
	if 'username' in session: ## do not change the 'username'
		labels, data = useCarparkData()
		return render_template('dashboard.html', data=data, labels=labels)  # render a template
	else: 
		return 'You are not logged in'

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('login'))

def useCarparkData():
	details = webapi.getCarparkAvailability('2019-12-31T09:54:15')
	top10 = details['items'][0]['carpark_data']
	labels, data = [], []
	for each in top10: 
		labels.append(each['carpark_number'])
		data.append(int(each['carpark_info'][0]['total_lots']))
	labels, data = labels[:10], data[:10]
	return labels, data

# start the server with the 'run()' method
if __name__ == '__main__':
	app.secret_key = 'secret123'
	app.run(debug=True)