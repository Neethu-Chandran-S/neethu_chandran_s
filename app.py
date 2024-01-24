from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('prediction',methods=['GET','POST'])
def predict():
    if request.method=='POST':
       input_vector= request.form['input vector']
       print(input_vector)
    return render_template('prediction.html')
  

if __name__=='__main__':
    app.run()