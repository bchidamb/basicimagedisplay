'''
This is a basic image displayer built in Flask. Whenever the homepage is
accessed, one of five images is selected at random and displayed.

Created by Bhairav Chidambaram
'''

from flask import Flask, render_template
from random import randint

app = Flask(__name__)

# Files stored in \static directory.
files = ["ostrich.jpg", "owl.jpg", "parrot.jpg", "swan.jpg", "toucan.jpg"]

@app.route('/')
def index():
    i = randint(0, 4)
# HTML templates stored in \templates directory.
    return render_template("images.html", filename = "static\\" + files[i], \
                           description = files[i][:-4])

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
