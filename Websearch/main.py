from re import search
from turtle import title
from flask import Flask , render_template , request, redirect ,url_for

app = Flask(__name__)
class urlinfo:
    def __init__(self,id,link,description,title) -> None:
        self.ref=link
        self.id=id
        self.description=description
        self.title=title
searchquery=""
urls=[]
url=urlinfo(1,"http://google.com","hi iam google","click google")
urls.append(url)
@app.route('/')
def main():
    response= render_template("index.html"  )
    
    return response

@app.route('/urlspage')
def urllink():
    response= render_template("urlspage.html",urls=urls  )
    return response

@app.route('/search',methods=["POST"])
def search():
    global searchquery 
    searchquery= request.form["searchquery"] 
    return redirect(url_for("urllink"))





app.run(debug=True) 
        