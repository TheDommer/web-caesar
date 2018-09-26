from flask import Flask, request, redirect
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
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <h1>Caesar</h1>
    <form method ='POST'>
    <label for="rot">Rotate by:</label>
    <input name="rot" type="text" value="0">
    <br>
    <label>Text input</label>
    <textarea name="text">{0}</textarea > 
    <input type="submit"/>
    </form>
    </body>
</html>        
"""


@app.route("/", methods=['POST'])
def encrypt(): 
    text = request.form['text'] #need to use grab methods for 'post' 
    #print(text)
    #tried using  and got 'TypeError: string indices must be integers'
    text=str(text)
        
    rot = request.form['rot'] #validate this for integer 
    rot=int(rot)
    ###need to add form.format stuff   

    coded_string = rotate_string(text, rot)
    final_string= coded_string.format('text')
    #print (final_string)
    return form.format(final_string)
    #store values of request parameters store
    #convert data type if needed 
    #encrypt value of text using 'rotate_string'
    #return encrypted string wrapped in <h1>



    # Within encrypt, store the values of these request 
    # parameters in local variables, converting data types as necessary. 
    # Then, encrypt the value of the text parameter using rotate_string. 
    # Return the encrypted string wrapped in <h1> tags, to be rendered in the browser.

app.run()