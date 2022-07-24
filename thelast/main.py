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

 # data base here 
import sqlite3

#create data base and connect
db=sqlite3.connect("app.db")

# create the tables and fields 
#db.execute("CREATE TABLE if not exists BOOKS (Name TEXT,Bid INTEGER,Price INTEGER,Author TEXT )")

# setting up the cursor
cr=db.cursor()
cr.execute("CREATE TABLE if not exists BOOKS (Name TEXT,Bid INTEGER,Price INTEGER,Author TEXT )")

# Inserting data 
cr.execute("INSERT INTO BOOKS(Name,Bid,Price,Author) VALUES('BOOK1',1,100,'AHMED')")

my_list=["book1","book2","book3"]
for key,user in enumerate(my_list):
    cr.execute(f"INSERT INTO BOOKS(Name,Bid,Price,Author) VALUES('{user}',{key},{key},'{user}')")
# retrieveing data feom data base 

cr.execute("select Name,Bid from BOOKS ")
print(cr.fetchone()) # retrieve single element from the last query
print(cr.fetchone()) # retrieve another element from the last query
# if there not exist reurn None
# return all rows in form of list of tubles 
print(cr.fetchall())
# if you want to retrive a fixed number of rows 
#print("fetch many \n")
#print(cr.fetchmany(5)) # return first five rows



# save commit changes
db.commit()
db.close()
# close data base 
 # end of data base 
#sr="Untitled-1"
#images=[]
#s="<img src='"+"{"+"{"+"url_for( \"static\" , filename=" + sr +""+")}"+"}"+"' alt=\"\">"
#book=bookinfo(1,"medo","100","pp",sr)        
#book1=bookinfo(1,"medo","100","pp",sr)        
books=[]
purchases =[]
filteritems =[]
sectionsname =[]

#books.append(book)
#books.append(book1)


@app.route('/')
def main():
    response= render_template("mainpage.html" , title="main page",books=books,custom_css="main",sectionsname=sectionsname  )
    return response

@app.route('/admin')
def admin():
    response= render_template("admin.html" , title="admin page",books=books,custom_css="admin",sectionsname=sectionsname )
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
    return redirect(url_for("admin"))

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


@app.route('/filter',methods=["POST"])
def filter():
    bookname= request.form["filtertype"]
    if bookname == "ALL":
       return redirect(url_for("main"))
    print(bookname)
    global books
    global filteritems
    filteritems.clear()
    for book in books:
        if book.author == bookname :
            print("found")
            filteritems.append(book)
    return redirect(url_for("formfilter"))


@app.route('/dofilter')
def formfilter():
    global filteritems
    response= render_template("mainpage.html" , title="main page",books=filteritems,custom_css="main" , sectionsname=sectionsname )
    return response


@app.route('/addsec',methods=["POST"])
def SectionNamea():
    global sectionsname
    secname= request.form["SectionName"]
    sectionsname.append(secname)
    return redirect(url_for("admin"))
            

app.run(debug=True) 

