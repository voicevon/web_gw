import os
import subprocess




from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # body = '<body style="background-color:powderblue;">'
    body = '<body style="color:white; link-color:green">'
    body += 'Text only,  <a href="http://voicevon.vicp.io:5000/ls">Hello World</a>'
    return (body)

@app.route('/shell_command')
def welcome():
   return ('welcome')
@app.route('/ls')
def ls():
    # useless_cat_call = subprocess.run(["cat"], stdout=subprocess.PIPE, text=True, input="Hello from the other side")
    useless_cat_call = subprocess.run(["cat"], stdout=subprocess.PIPE, text=True)
    return (useless_cat_call)
    
if __name__ == '__main__':
#    app.run(host='0.0.0.0')
ls()
