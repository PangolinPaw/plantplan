from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    placeholder = 'hello world'
    return render_template(
        'home.html'
    )

if __name__ == '__main__':
    app.run( debug=True )

