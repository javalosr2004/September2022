import asyncio
import time

from pyppeteer import launch
from urllib.parse import urlparse



WEBSITE_LIST = [
    'http://envato.com',
    'http://amazon.co.uk',
    'http://amazon.com',

]

start = time.time()

async def fetch(url):
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto(f'{url}', {'waitUntil': 'load'})
    await page.screenshot({'path': f'{urlparse(url)[1]}.png'})
    await browser.close()

async def run():
    tasks = []

    for url in WEBSITE_LIST:
        task = asyncio.create_task(fetch(url))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)
    #print(responses)

#asyncio.get_event_loop().run_until_complete(fetch('http://yahoo.com'))
asyncio.run(run())

print(f'It took {time.time()-start} seconds.')