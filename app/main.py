from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)