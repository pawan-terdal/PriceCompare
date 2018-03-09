from flask import Flask, render_template, url_for, request, redirect
from exactSearch import exactS
from generalSearch import generalS

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def start():
	if request.method == 'GET':										#Displays the home page.
		return render_template('HomePage.html')

	if request.method == 'POST':
		key = request.form['search']                				#Assigning the Search String to key.
		if request.form['submit'] == 'exactSearch':					
			return redirect(url_for('exact_search', key = key))		#If Exact Search is clicked, redirect to exact_search.
		elif request.form['submit'] == 'generalSearch':
			return redirect(url_for('general_search', key = key))   #If General Search is clicked, redirect to general_search.


@app.route('/esearch', methods = ['GET'])
def exact_search():													
	if request.method == 'GET':										
		key = request.args.get('key', None)							#Retrieving the key.
		SearchString = key
		results = ""
		results = exactS(SearchString).split('\n')					#Calling the method exactS in exactSearch.py.
		return render_template('ShowItems.html', results = results)
		

@app.route('/gsearch', methods = ['GET'])
def general_search():
	if request.method == 'GET':
		key = request.args.get('key', None)							#Retrieving the key.
		SearchString = key
		results = ""
		results = generalS(SearchString).split('\n')				#Calling the method generalS in generalSearch.py.
		return render_template('ShowItems.html', results = results)		

if __name__ == "__main__":
	app.run(debug = True)