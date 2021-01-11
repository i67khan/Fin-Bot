import json
import discord
import requests
import bs4


client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

def get_stock(id):
    r = requests.get('https://finance.yahoo.com/quote/' + id +'?p=' + id + '&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello from Ibrahim!')

    if message.content.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('!stock'):
        if len(message.content.split()) != 1:
            txt = message.content.split()[1]
            stock = get_stock(txt)
            await message.channel.send(stock)
        else:
            print('A valid stock code must be included in this command')


client.run('Nzk2NDgwODM5Mjk3OTI1MTUz.X_YilQ.RPbVu_sSHOBw7RfH14TKmxPtZmc')
