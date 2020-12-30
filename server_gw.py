from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # https://www.techiediaries.com/flask-tutorial-templates/
    return render_template("index.html", message="Hello Flask!")


@app.route('/exec')
def exec():
    content = '<form action="/exec" method="get">'
    content += '<input type="text" name="command" length = 40>'
    content += '<input type="submit" value="Exec" />'
    content += '<p>'
    content += '</form><hr>'
    # content = ''
    raw_command = request.args.get('command', default='')
    command = raw_command.split(' ')
    # print(command)
    # return (command)
    content += raw_command
    content += '<hr> <pre>'

    # raw_response = subprocess.run(command, stdout=subprocess.PIPE)
    # response = str(raw_response.stdout, 'utf-8')
    response = "get command :" + str(command)
    # print(command,response)
    content += response.replace('\n', '<p>')
    return (content)


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run()
