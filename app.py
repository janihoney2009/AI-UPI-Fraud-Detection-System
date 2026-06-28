from flask import Flask, render_template,request 

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    result = ""

    if request.method =="POST":
        amount = int(request.form["amount"])
        time = request.form["time"]
        new_user = request.form["new_user"]
        multiple = request.form["multiple"] 
 
        if amount > 50000:
            result = "Fraud Alert!"
        elif time == "Night" and new_user == "Yes":
            result = "Suspicious Transaction!"
        elif multiple == "Yes":
            result = "Multiple Transaction Detected!"
        else:
            result = "Safe Transaction"        

    return render_template("index.html",result=result)


if __name__=="__main__":
    app.run(debug=True)