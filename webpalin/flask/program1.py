from flask import Flask, render_template, flash, redirect, request, session, abort

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/about_/")

def about():
    return render_template('about_.html')

if __name__=="__main__":
    app.run(debug=True)

