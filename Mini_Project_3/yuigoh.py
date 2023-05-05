import pprint
import requests
from flask import Flask,redirect,url_for,request,render_template
import json

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
    cardByPrice = {}
    for card in jsoncards['data']:
        if float(searchPrice) >= float(card['card_prices'][0]['amazon_price']):
            cardByPrice[f'{card["name"]}'] = card['card_prices'][0]['amazon_price']
    if cardByPrice:
        return dict(sorted(cardByPrice.items(), key=lambda item: float(item[1])))
    else:
        return False

@app.route('/')
@app.route('/start')
def start():
    return render_template('yugiohlandingpage.html')

@app.route('/search',methods=['POST'])
def search():
    if request.method == 'POST':
        name = request.form.get('name')
        print(name)
        card = get_card(name)
        if card:
            return card
        else:
            return json.loads('{}')

@app.route('/imgSearch',methods=['POST'])
def imgSearch():
    if request.method == 'POST':
        name = request.form.get('name')
        cardImg = get_img(name)
        if cardImg:    
            return render_template("yugiohimage.html" ,imageURL = cardImg)
        else:
            return json.loads('{}')

@app.route('/typeSearch',methods=['POST'])
def typeSearch():
    if request.method == 'POST':
        Type = request.form.get('type')
        cardType = get_all_byType(Type)
        if cardType:
            return cardType
        else: 
            return json.loads('{}')

@app.route('/priceSearch',methods=['POST'])
def priceSearch():
    if request.method == 'POST':
        price = request.form.get('price')
        cardsByPrice = get_card_byPrice(price)
        if cardsByPrice:
            return cardsByPrice
        else:
            return json.loads('{}')

def main():
    get_cards()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2224,debug=True)
