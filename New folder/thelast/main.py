from re import search
from turtle import title
from flask import Flask , render_template , request, redirect ,url_for

app = Flask(__name__)
task=[]
id=0
class bookinfo:
    def __init__(self,id,name,price,author,source) -> None:
        self.name=name
        self.id=id
        self.price=price
        self.author=author
        self.source=source


#sr="Untitled-1"
#images=[]
#s="<img src='"+"{"+"{"+"url_for( \"static\" , filename=" + sr +""+")}"+"}"+"' alt=\"\">"
#book=bookinfo(1,"medo","100","pp",sr)        
#book1=bookinfo(1,"medo","100","pp",sr)        
books=[]
purchases =[]

#books.append(book)
#books.append(book1)


@app.route('/')
def main():
    response= render_template("mainpage.html" , title="main page",books=books,custom_css="main"  )
    return response

@app.route('/admin')
def admin():
    response= render_template("admin.html" , title="admin page",books=books,custom_css="admin" )
    return response

@app.route('/add',methods=["POST"])
def add():
    bookname= request.form["BookName"]
    imagname= request.form["AuthorName"]
    BookPrice= str(request.form["BookPrice"])
    Section= request.form["Section"]
    new_book= bookinfo(1,bookname,BookPrice,Section,imagname)
    global books
    books.append(new_book)
    return redirect(url_for("main"))

@app.route('/purchase',methods=["POST"])
def purchase():
    bookname= request.form["bookname"]
    print(bookname)
    global books
    global purchases
    for book in books:
        if book.name == bookname :
            print("found")
            purchases.append(book)
            break

    for book in purchases:
        print(book.price)

    return redirect(url_for("main"))

@app.route('/purchase_c')
def purchase_c():
    global purchases
    cost=0
    if len(purchases) :
        for book in purchases:
            cost+=int(book.price)
    print(cost)
    response= render_template("purchase.html" , title="Purchase page",books=purchases,custom_css="purchase" , cost=str(cost) )
    return response 

@app.route('/del',methods=["POST"])
def delele_item():
    bookname= request.form["bookname"]
    print(bookname)
    global books
    global purchases
    c=0
    for book in purchases:
        if book.name == bookname :
            print("found")
            del (purchases[c])
            break
        c+=1

    for book in purchases:
        print(book.price)

    return redirect(url_for("purchase_c"))


@app.route('/confirm',methods=["POST"])
def confirm():
    global purchases
    
    purchases.clear() 
        

    for book in purchases:
        print(book.price)

    return redirect(url_for("purchase_c"))



app.run(debug=True) 

