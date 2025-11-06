from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Chris!! Also, I like poutine!"

if __name__ == '__main__':
    app.run()
