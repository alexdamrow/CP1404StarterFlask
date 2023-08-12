from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f'Hello {name}'


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * (9 / 5)) + 32


@app.route('/f/<celsius>')
def convert(celsius=0):
    return f"{celsius} celsius = {convert_celsius_to_fahrenheit(float(celsius))} fahrenheit"


if __name__ == '__main__':
    app.run()
