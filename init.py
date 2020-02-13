from flask import Flask, render_template
import paymentMethod
from flask import jsonify
import json
app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello():
    allPaymentMethods = paymentMethod.getAll()
    print(allPaymentMethods)
    allPaymentMethods = json.dumps(str(allPaymentMethods))

    print(allPaymentMethods)
    return render_template('dropin.html',allPaymentMethods=allPaymentMethods)


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()