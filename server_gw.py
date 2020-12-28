 
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # https://www.techiediaries.com/flask-tutorial-templates/
    return render_template("index.html", message="Hello Flask!");   
@app.route('/exec')
def exec():
    # content = '<form action="/exec" method="post">'
    # content += '<input type="text" name="command"/>'
    # content += '<input type="submit" value="Execute">'
    # content += '</form><hr>'
    content = '<input type="text" name="input" length = 40>'
    content += '<input type="button" value="Exec" onclick="location.href =' 
    #content += "'/abc'" + '"/>'
    next_command="ls -l"
    content += "'/exec?command=" + next_command +"'" + '"/>'
    content += '<p>'
    # content = ''
    raw_command = request.args.get('command', default='')
    command = raw_command.split(' ')
    #print(command)
    # return (command)
    content +=  raw_command 
    content += '<hr> <pre>'

    raw_response = subprocess.run(command, stdout=subprocess.PIPE)
    response = str(raw_response.stdout, 'utf-8')
    #print(command,response)
    content += response.replace('\n','<p>')
    return (content)

@app.route('/ls')
def ls():
    response = subprocess.run(["ls","-l"], stdout=subprocess.PIPE)
    ss = str(response.stdout, 'utf-8')
    rr = ss.replace('\n','<p>')
    return (rr)
    
if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run()
