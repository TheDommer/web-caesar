from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return form 

form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <h1>Caesar</h1>
    <form method ='POST'>
    <label>Rotate by:</label>
    <input name="rot" type="text" value="0"/>
    <br>
    <label>Text input</label>
    <input name="text" type="textarea"/>
    <input type="submit"/>
    </body>
</html>        
"""
@app.route("/", methods=['POST'])
def encrypt():
    #store values of request parameters
    #convert data type if needed
    #encrypt value of text using 'rotate_string'
    #return encrypted string wrapped in <h1>

app.run()
