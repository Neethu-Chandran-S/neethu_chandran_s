from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('prediction',methods=['GET','POST'])
def predict():
    
    return 'Neethu'

if __name__=='__main__':
    app.run()