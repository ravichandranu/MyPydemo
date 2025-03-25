from flask import Flask,render_template,request,jsonify

app=Flask(__name__)


items=[
    {'id':1,'name':'Ravi','desc':'one'},
    {'id':2,'name':'Anand','desc':'two'}
       ]

@app.route("/items",methods=['GET'])
def get_items():
    return jsonify(items)

@app.route("/items1/<int:itemid>",methods=['GET'])
def get_items1(itemid):
    item=next((item for item in items if item['id']==itemid),None)
    if item is None:
        return jsonify({"error":"Not found"})
    return jsonify(item)
          

@app.route("/")
def Home():
    return "<html></h1><b>Welcome to Home Page</b></h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")
    
@app.route("/form",methods=['GET','POST'])
def forms():
    if request.method=="POST":
        name=request.form['name']
        return f"Hello {name}"
    return render_template("Form.html")


@app.route("/submit",methods=['GET','POST'])
def submits():
    if request.method=="POST":
        name=request.form['name']
        return f"Hello {name}"
    return render_template("Form.html")


@app.route("/Success/<int:score>")
def onsuccess(score):
    return "you have entered "+ str(score)

@app.route("/Success1/<int:score>")
def onsuccess1(score):
    res=""
    if score>40:
        res="psss"
    else:
        res="Fail"
    exp={'Score':score,"res":res}

    return render_template("results.html",results=score)


if __name__=="__main__":
    app.run(debug=True)
