from flask import render_template, request
from create_repo import app
import create_repo.controllers

errorMessage = "Repo Exists Already!"

@app.route('/', methods=['GET', 'POST'])
def index():
	r_list = create_repo.controllers.listRepos()
	if request.method == 'POST':
		repo_name = request.form['repo_name']
		if (create_repo.controllers.createRepo(repo_name)):
			successMessage = "Success! clone the repository at pi@192.168.10.1:/home/pi/pigit/repos/" + repo_name
			return render_template("index.html", sucess=successMessage, r_list=r_list)
		else:
			return render_template("index.html", error=errorMessage, r_list=r_list)
	return render_template("index.html", r_list=r_list)