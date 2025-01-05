from flask import Flask, jsonify, request
import requests
from APIKEY import apiKey

API=apiKey  #getting the api key value stored in variable

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    data = request.get_json()   #fetch data
    print(data)

    base_currency=data['queryResult']['parameters']['unit-currency']['currency']   #Base Currency
    base_amount=data['queryResult']['parameters']['unit-currency']['amount']       #Base amount

    target_currency=data['queryResult']['parameters']['currency-name']               #Target currency
    conversion_factor= fetch_conversion_factor(base_currency,target_currency)        # fetch the conversion factor

    final_amount= base_amount * conversion_factor                                    #Final converted value
    print(f'{base_amount} {base_currency} is {final_amount} {target_currency} in real time')
    #generate response to forward to chatbot
    response = {
        'fulfillmentText': f'{base_amount} {base_currency} is {final_amount:.2f} {target_currency} in real time'
    }

    return jsonify(response)

def fetch_conversion_factor(base_currency, target_currency):

    url= f'https://api.currencyapi.com/v3/latest?apikey={API}&currencies={target_currency}&base_currency={base_currency}'

    response= requests.get(url)  #get response
    response= response.json()    #convert to json

    conversion_factor= response['data'][f'{target_currency}']['value']
    print(conversion_factor)
    return conversion_factor


if __name__ == '__main__':
    app.run()