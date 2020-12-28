
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # https://www.techiediaries.com/flask-tutorial-templates/
    return render_template("index.html", message="Hello Flask!");   
@app.route('/exec')
def exec():
    command = request.args.get('command', default='')
    args = request.args.get('args', default='')
    target =  command + ' ' + args
    target += '<hr> <pre>'

    response = subprocess.run([command,args], stdout=subprocess.PIPE)
    ss = str(response.stdout, 'utf-8')
    print(command,ss)
    target += ss.replace('\n','<p>')
    return (target)

@app.route('/ls')
def ls():
    response = subprocess.run(["ls","-l"], stdout=subprocess.PIPE)
    ss = str(response.stdout, 'utf-8')
    rr = ss.replace('\n','<p>')
    return (rr)
    
if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run()
