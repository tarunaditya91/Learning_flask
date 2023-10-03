from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__,template_folder='templates')

todos=[]


@app.route("/")
def index():
    name="tarun"
    return render_template("index.html",name2=name)


if __name__=='__main__':
    app.run(debug=True)
