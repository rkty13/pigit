from flask import Flask, render_template
import os
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route('/')
def index():
	(stdout, stderr) = Popen(["ls", "../"], stdout=PIPE).communicate()
	return render_template("index.html", stdout=stdout)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host="0.0.0.0", port=port, debug=True)