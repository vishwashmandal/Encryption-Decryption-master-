from flask import Flask,request,redirect,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from utils import algo,decrypt
import json

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# db.create_all()

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     desc = db.Column(db.String(500), nullable=True)
#     date_created = db.Column(db.DateTime,default=datetime.utcnow)

#     def __repr__(self):
#         return str(self.id)+" "+self.title






@app.route("/",methods=['GET', 'POST'])
def main():
    try:
        result=""
        key1=""
        key2=""
        #this post method we are not using
        if request.method=='POST':
            # print(request.POST)
            result=algo(request.form['key1'],request.form['key2'],request.form['text'])
            key1=request.form['key1']
            key2=request.form['key2']
            # result=decrypt(request.POST['key1'],request.POST['key2'],request.POST['text'])

        return render_template('index.html',result=result ,k1=key1,k2=key2)
    except:
        return render_template('4oo.html')


#this route we are not using.
@app.route("/decrypt/",methods=['GET', 'POST'])
def Decrypt():
    try:
        res=""
        res=decrypt(request.args['k1'],request.args['k2'],request.args['text1'])
    
        return render_template('index.html',res=res)
    except:
        return render_template('4oo.html')



@app.route("/api/",methods=['GET', 'POST'])
def apiview():
    if request.method == "POST":
        result=''
        action='en'
        try:
            data = json.loads(request.data)
            if data['action']=='en':
                result=algo(data['key1'],data['key2'],data['text'])

            elif data['action']=='dy':
                result=decrypt(data['key1'],data['key2'],data['text'])
                action='dy'
        except:
            result=''
        d={'result':result,'action':action}
        return jsonify(d)






if __name__ == '__main__':
    app.run(debug=True,port=8000)