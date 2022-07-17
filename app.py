from flask import Flask
app = Flask(__name__)

#create route
@app.route('/')
def hello_world():
    return 'Bitch it works'

@app.route('/<page_id>')
def yo(page_id):
    return 'hello '+page_id

if __name__ =="__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0' , port=8080)

