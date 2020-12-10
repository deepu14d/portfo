from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/<string:html_page>')    #instead of copy pasting and initializing route for every button we can just use it
def page(html_page):
	return render_template(html_page) 

def write_data(data):
	with open('database.txt', 'a') as db:
		Name = data['name']
		Email = data['email']
		Message = data['message']
		file = db.write(f'\n{Name}, {Email}, {Message} ')

def write_csv(data):
	with open('database.csv', mode='a') as db2:  # newline=''
		Name = data['name']
		Email = data['email']
		Message = data['message']
		csv_file = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_file.writerow([Name, Email, Message])

@app.route('/contact_me', methods=['POST', 'GET'])
def contact_me():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_csv(data)
			print(data)
			return redirect('/thankyou.html#contact')
		except:
			return 'some error occured. \n unable to save to database.'
			
	else:
		return 'Something went wrong. Try again.'

