from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") #by returning the template from the template folder called index html we open that template.
@app.route('/cakes')
def cakes():
    return 'yummy cakes'



if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
    
# to access the webserver, type : https://127.0.0.1:5000/
#127.0.0.1 means home, ( this computer ) and :5000 means port 5000 which is the port
# that the websever is running on.

#@app.route('/") determines the entery point the / means the root of the website, so
#homepage
#def index() is the name we give to the route/ it was called index bc its the index
# of the website.

