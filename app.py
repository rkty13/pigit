from flask import Flask, render_template
import os
from subprocess import Popen, PIPE

app = Flask(__name__)

def createRepo(repo_name, user_list):
	print "TODO"

@app.route('/', methods=["POST"])
def index():
	if request.method == 'POST':
		form = request.form
		repo_name = form['repo_name']
		user_list = []
		for i in range(form['num_users']):
			user_list.append(form['user' + str(i)])
		createRepo(repo_name, user_list)

	(stdout, stderr) = Popen(["ls", "../"], stdout=PIPE).communicate()
	return render_template("index.html", stdout=stdout)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host="0.0.0.0", port=port, debug=True)