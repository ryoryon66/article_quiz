from flask import Flask, jsonify, render_template,request
import utility
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/article')
def article():
    return render_template('practice_article.html')

@app.route('/tense')
def tense():
    return render_template('practice_tense.html')

@app.route('/make_article_quiz',methods = ["POST"])
def make_article_quiz():

    material = request.json['material']  
    print(material)


    return jsonify({'quiz':utility.make_article_quiz(material)})
    
@app.route('/make_tense_quiz',methods = ["POST"])
def make_tense_quiz():

    material = request.json['material']  
    print(material)


    return jsonify({'quiz':utility.make_tense_quiz(material)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8889, debug = False)                                                                  
    #app.run(host='127.0.0.1', port=8888, debug=True)   _
