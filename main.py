from flask import Flask,request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form = """

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
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
     <!-- create your form here -->
     <form action="/" method= "POST"> 
     <label for="rot"> Rotate by:</label>
     <input type='text' id='rot' name="rot" min='0'>
     <br>
     <textarea name="text" rows="10" cols ="30"></textarea>
     <input type="submit">
     </form>
     </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rot=int(request.form["rot"])
    text=request.form["text"]
    encrypted_text= rotate_string(text,rot)
    return "<h1>" +  encrypted_text + "</h1>"



    @app.route("/")
def index():
    return form

app.run()
