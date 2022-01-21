import telebot
import requests

abreeds={'Abyssinian': 'abys', 'Aegean': 'aege', 'American Bobtail': 'abob', 'American Curl': 'acur', 'American Shorthair': 'asho', 'American Wirehair': 'awir', 'Arabian Mau': 'amau', 'Australian Mist': 'amis', 'Balinese': 'bali', 'Bambino': 'bamb', 'Bengal': 'beng', 'Birman': 'birm', 'Bombay': 'bomb', 'British Longhair': 'bslo', 'British Shorthair': 'bsho', 'Burmese': 'bure', 'Burmilla': 'buri', 'California Spangled': 'cspa', 'Chantilly-Tiffany': 'ctif', 'Chartreux': 'char', 'Chausie': 'chau', 'Cheetoh': 'chee', 'Colorpoint Shorthair': 'csho', 'Cornish Rex': 'crex', 'Cymric': 'cymr', 'Cyprus': 'cypr', 'Devon Rex': 'drex', 'Donskoy': 'dons', 'Dragon Li': 'lihu', 'Egyptian Mau': 'emau', 'European Burmese': 'ebur', 'Exotic Shorthair': 'esho', 'Havana Brown': 'hbro', 'Himalayan': 'hima', 'Japanese Bobtail': 'jbob', 'Javanese': 'java', 'Khao Manee': 'khao', 'Korat': 'kora', 'Kurilian': 'kuri', 'LaPerm': 'lape', 'Maine Coon': 'mcoo', 'Malayan': 'mala', 'Manx': 'manx', 'Munchkin': 'munc', 'Nebelung': 'nebe', 'Norwegian Forest Cat': 'norw', 'Ocicat': 'ocic', 'Oriental': 'orie', 'Persian': 'pers', 'Pixie-bob': 'pixi', 'Ragamuffin': 'raga', 'Ragdoll': 'ragd', 'Russian Blue': 'rblu', 'Savannah': 'sava', 'Scottish Fold': 'sfol', 'Selkirk Rex': 'srex', 'Siamese': 'siam', 'Siberian': 'sibe', 'Singapura': 'sing', 'Snowshoe': 'snow', 'Somali': 'soma', 'Sphynx': 'sphy', 'Tonkinese': 'tonk', 'Toyger': 'toyg', 'Turkish Angora': 'tang', 'Turkish Van': 'tvan', 'York Chocolate': 'ycho'}
token = '5007134020:AAGFOdHS5REdnOLQ-Y7nK0qmwX9cJzvHvlc'
headers={'x-api-key':'68348fcf-3a20-43e2-ac0b-96a9a9204e79'}
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def show_cat(message):
    if message.text=='cat':
        a=requests.get('https://api.thecatapi.com/v1/images/search',headers).json()
        bot.send_photo(message.from_user.id, a[0].get('url'))

    if message.text=='breeds':
        tem=''
        for a in abreeds:
            tem+=a+':/'+abreeds.get(a)+'\n'
        bot.send_message(message.from_user.id,tem)
    if list(abreeds.keys()).count(message.text)>0 or list(abreeds.values()).count(message.text[1::])>0:
        if message.text[0]=='/':
            a = requests.get('https://api.thecatapi.com/v1/images/search?breed_id=' + message.text[1::],headers).json()
            bot.send_photo(message.from_user.id,a[0].get('url'))
        else:
            a=requests.get('https://api.thecatapi.com/v1/images/search?breed_id='+abreeds.get(message.text),headers).json()
            bot.send_photo(message.from_user.id,a[0].get('url'))
    if message.text=='help':
        bot.send_message(message.from_user.id,'Type breeds or /breeds to get list of breeds'+'\n'+'Type cat to get a random cat'+'\n'+'Type a cat breed of a short id to get a picture of cat of desired breed')


















bot.polling(none_stop=True, interval=0)