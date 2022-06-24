from flask import Flask,redirect,url_for,render_template,request
import util

# jinja2 technique
'''
{{ value }}expression 
{%  %}statment
{#.....#}comment

'''


app=Flask(__name__)


@app.route('/')
def fun():
    location=util.load_location()
    
    return render_template('index.html',locations=location,pred=0)




@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        res=dict(request.form)
        loc=res['location']
        bhk=int(res['bhk'].split(' ')[0])
        bath=int(res['bath'].split(' ')[0])
        area=float(res['area'])
        predicted_val=util.predict_price(loc,bhk,area,bath)
        locations=util.load_location()
        return render_template('index.html',locations=locations,pred=predicted_val,bath=bath,bhk=bhk,
        area=area,loc=str(loc))





if __name__=='__main__':
    app.run()