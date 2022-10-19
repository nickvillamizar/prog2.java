from flask import Flask
from controller.list_se_controller import app_list_se

app = Flask(__name__)
app.register_blueprint(app_list_se)


"""
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/example')
def get_message():  # put application's code here
    return 'Hola Campeones'
@app.route('/example/message2')
def get_message2():  # put application's code here
    return 'Hola a ponersen las pilas desde python'
@app.route('/example/concatmessage/<word1>/<word2>')
def concat_message(word1:str,word2:str):
    return 'En la jugada '+word1 +' '+word2
@app.route('/example/add/<num1>/<num2>')
def add(num1,num2):
    return str(int(num1)+int(num2))
"""
if __name__ == '__main__':
    app.run()


