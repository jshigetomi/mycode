import pprint
import requests
from flask import Flask,redirect,url_for,request,render_template
import pandas as pd
import json
import html

url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
cards = requests.get(url)
jsoncards = cards.json()

app = Flask(__name__)

def get_card(searchname):       
    for card in jsoncards['data']:
        if searchname.lower() == card['name'].lower():
            return card
    else:
        print(f"Name of card entered {searchname}: Name of cards {jsoncards['data'][0]['name']}")
        print("card not found")
        return False

def get_img(searchname):
    card = get_card(searchname)
    imageURLS = []
    if card:
        for url in card['card_images']:
            imageURLS.append(url['image_url'])
        return imageURLS
    else:
        return False

def get_all_byType(searchtype):
    cardType = []
    for card in jsoncards['data']:
        if searchtype.lower() == card['type'].lower():
            cardType.append(card)
    if cardType:
        return cardType
    else:
        return False

def get_card_byPrice(searchPrice):
    cardByPrice = {'name':[],
                   'price':[]}
    for card in jsoncards['data']:
        if float(searchPrice) >= float(card['card_prices'][0]['amazon_price']):
            cardByPrice['name'].append(card["name"])
            cardByPrice['price'].append(float(card['card_prices'][0]['amazon_price']))
    dataframe = pd.DataFrame.from_dict(cardByPrice)
    if cardByPrice:
        dataframe = dataframe.sort_values(by='price',ascending=False)
        return json.loads(dataframe.to_json(orient='split'))

    else:
        return False

@app.route('/')
@app.route('/start')
def start():
    return render_template('yugiohlandingpage.html')

@app.route('/search',methods=['POST','GET'])
def search():
    if request.method == 'GET':
        name = request.args.get('name')
    if request.method == 'POST':
        name = request.form.get('name')
        print(name)
    card = get_card(name)
    if card:
        return card
    else:
        return json.loads('{}')

@app.route('/imgSearch',methods=['POST','GET'])
def imgSearch():
    if request.method == 'GET':
        name = request.args.get('name')
        cardImg = get_img(name)
        if cardImg:
            return cardImg
        else:
            return json.loads('{}')
    if request.method == 'POST':
        name = request.form.get('name')
        cardImg = get_img(name)
        if cardImg:    
            return render_template("yugiohimage.html" ,imageURL = cardImg)
        else:
            return json.loads('{}')

@app.route('/typeSearch',methods=['POST','GET'])
def typeSearch():
    if request.method == 'GET':
        Type = request.args.get('type')
    if request.method == 'POST':
        Type = request.form.get('type')
    cardType = get_all_byType(Type)
    if cardType:
        return cardType
    else: 
        return json.loads('{}')

@app.route('/priceSearch',methods=['POST','GET'])
def priceSearch():
    if request.method == 'GET':
        price = request.args.get('price')
    if request.method == 'POST':
        price = request.form.get('price')
    cardsByPrice = get_card_byPrice(price)
    if cardsByPrice:
        return cardsByPrice
    else:
        return json.loads('{}')    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2224,debug=True)
