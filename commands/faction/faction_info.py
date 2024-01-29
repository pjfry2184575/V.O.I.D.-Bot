import requests
from guilded.ext import commands

from config import API_Key


async def faction_info(ctx):
    url = f'https://api.torn.com/faction/?selections=currency&key={API_Key}&comment=TryItPage'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        faction_id = data.get('faction_id')
        points = "{:,}".format(data.get('points', 0))
        money = "{:,}".format(data.get('money', 0))

        if faction_id is not None and points is not None and money is not None:
            message = f'Planet-Express Information\nFaction ID: {faction_id}\nPoints: {points}\nMoney: {money}'
            await ctx.send(message)
        else:
            await ctx.send('Some information is missing in the API response.')
    else:
        await ctx.send(f'Error: {response.status_code}')
