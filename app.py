from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)

def createRepo(repo_name, user_list):
	subprocess.call(["touch", "repos/test.txt"])

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		repo_name = request.form['repo_name']
		user_list = []
		user_list.append(request.form['user1'])
		createRepo(repo_name, user_list)
		return render_template("index.html")

	return render_template("index.html")

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host="0.0.0.0", port=port, debug=True)