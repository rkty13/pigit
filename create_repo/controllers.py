import subprocess
from subprocess import Popen, PIPE

DIR = "repos/"

def checkRepoExists(repo_name):
	(stdout, stderr) = Popen(["ls", "repos"], stdout=PIPE).communicate();
	repo_list = stdout.split("\n")
	if repo_name in repo_list:
		return True
	else:
		return False

def createRepo(repo_name):
	if (not checkRepoExists(repo_name)):
		repo_dir = DIR + str(repo_name)
		subprocess.call(["mkdir", repo_dir])
		subprocess.call(["git", "init", "--bare", repo_dir + "/.git"])
		subprocess.call(["touch", DIR + ".test.txt"])
		return True
	else:
		return False

def listRepos():
	(stdout, stderr) = Popen(["ls", "repos"], stdout=PIPE).communicate();
	repo_list = stdout.split("\n")
	return repo_list