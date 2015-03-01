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

def createRepo(repo_name):
	if (not checkRepoExists(repo_name)):
		repo_dir = "repos/" + str(repo_name) + ".git"

		# Create repository directory
		subprocess.call(["mkdir", repo_dir])

		# Create init git repository
		subprocess.call(["git", "init", "--bare", repo_dir + "/.git"])

		subprocess.call(["touch", "repos/test.txt"])
		return True
	else:
		return False

def listRepos():
	(stdout, stderr) = Popen(["ls", "repos"], stdout=PIPE).communicate();
	repo_list = stdout.split("\n")
	return repo_list


@app.route('/', methods=['GET', 'POST'])
def index():
	r_list = listRepos()
	if request.method == 'POST':
		repo_name = request.form['repo_name']
		if (createRepo(repo_name)):
			successMessage = "Success! clone the repository at pi@192.168.10.1:/home/pi/pigit/repos/" + repo_name
			return render_template("index.html", sucess=successMessage, r_list=r_list)
		else:
			errorMessage = "Repo Exists Already!"
			return render_template("index.html", error=errorMessage, r_list=r_list)

	return render_template("index.html", r_list=r_list)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host="0.0.0.0", port=port, debug=True)
