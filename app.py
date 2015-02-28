from flask import Flask, render_template, request
import os
import subprocess
from subprocess import Popen, PIPE

app = Flask(__name__)

def checkRepoExists(repo_name):
	(stdout, stderr) = Popen(["ls", "repos"], stdout=PIPE).communicate();
	repo_list = stdout.split("\n")
	if repo_name in repo_list:
		return True
	else:
		return False

def createRepo(repo_name, user_list):
	if (not checkRepoExists(repo_name)):
		repo_dir = "repos/" + str(repo_name)
		subprocess.call(["groupadd", repo_name])
		for user in user_list:
			subprocess.call(["groups", user, "-aG", repo_name])
		subprocess.call(["mkdir", repo_dir])
		subprocess.call(["git", "init", "--bare", repo_dir + "/.git"])
		subprocess.call(["touch", "repos/test.txt"])
		return True
	else:
		return False

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		repo_name = request.form['repo_name']
		user_list = []
		user_list.append(request.form['user1'])
		if (createRepo(repo_name, user_list)):
			return render_template("index.html")
		else:
			return render_template("index.html", error="Repo Exists")

	return render_template("index.html")

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host="0.0.0.0", port=port, debug=True)