from flask import Flask
app = Flask(__name__)
@app.route("/")

def main():
    fname = "homepage.html"
    html_file = open(fname, 'r', encoding='utf-8')
    source_code = html_file.read() 
    return source_code
    
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8080)