from flask import Flask, render_template,request, redirect, session, flash
app = Flask(__name__)
app.secret_key="letsdoitagainsometime"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/result",methods=['POST'])
def didplayInfo():
	print ("Received POST")
	print(request.form)
	session["response"] = [request.form["name"],request.form["city"],request.form["lang"],request.form["textBox"]]
	if len(request.form["name"]) < 1:
		flash("name Cannot be empty!")
		return redirect("/")
	if request.form["city"] == "":
		flash("Must Select city!!")
		return redirect("/")
	if request.form["lang"] == "":
		flash("Must select favorite Language!")
		return redirect("/")
	else:
		w = session["response"][0]
		x = session["response"][2]
		y = session["response"][1]
		z = session["response"][3]
		flash("Success all info satisfies")
		return render_template('/result.html', passn= w, passl= x, passc = y, passt= z)
	


	

@app.route("/danger/")
def danger():
	print("*********\n"* 80)
	print("a user tried to visit /danger.  we have redirected the user to /")
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)

