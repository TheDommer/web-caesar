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
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
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
    <textarea type="text" name="text" {0}></textarea {0}>
    <input type="submit"/>
    </form>
    </body>
</html>        
"""
@app.route("/", methods=['POST'])
def encrypt(): 
    text = request.args.get('text')
    #tried using text = request.form['text'] and got 'TypeError: string indices must be integers'
    for char in text: #getting 'TypeError: 'NoneType' object is not iterable' traced to this line 
        if not char[text].isalpha(): 
            text_error = "Please enter sentance"
            return ("/?error=" + text_error)
    else:
        text=str(text)
        
    rot = request.args.get("rot") #validate this for integer 
    if not is_integer(rot):
        rot_error = "Please enter number"
        return ("/?error=" + rot_error)
    else:
        rot=int(rot)
    ###need to add form.format stuff   

    final_string = rotate_string(text, rot)
    return "<h1>final_string</h1>"
    #store values of request parameters store
    #convert data type if needed 
    #encrypt value of text using 'rotate_string'
    #return encrypted string wrapped in <h1>



    # Within encrypt, store the values of these request 
    # parameters in local variables, converting data types as necessary. 
    # Then, encrypt the value of the text parameter using rotate_string. 
    # Return the encrypted string wrapped in <h1> tags, to be rendered in the browser.

app.run()