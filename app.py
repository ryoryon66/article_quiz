from flask import Flask, jsonify, render_template,request
import utility
from flask_cors import CORS
import argparse



app.run(host=args.host, port=args.port, debug=args.debug)
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
    parser = argparse.ArgumentParser(description='Flask app arguments')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host address')
    parser.add_argument('--port', type=int, default=8889, help='Port number')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug = args.debug)                                                                  
_
