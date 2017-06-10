from flask import Flask, request
from ceasar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

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
          <form action="" method="post">
            <label for="rot">
                <strong>Rotate by:</strong>
                <input id="rot" type="text" name="rot" value="0" />
            </label>
            <textarea name="text"></textarea>
            <input type="submit" />

        </body>
    </html>

"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rotation = int(request.form["rot"])
    text = request.form["text"]
    encrypted_string = rotate_string(text, rotation)

    return "<h1>" + encrypted_string + "</h1>"

app.run()
