from re import T
from pyppeteer import launch
from typing import List
import asyncio

#launch browser
## go to educate page
### find search box (repeat)
    ###click search box
    ###type inside of it 
    ####wait for javascript to laod
    ####locate the title inside of the html
    ####return titles via list
###output

#print("====================== {} ======================".format(keyword))

keywords = ['python', 'opensource', 'virtual']

async def fetch_data(keyword):
    browser = await launch(headless = False, executablePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')

    page = await browser.newPage()
    await page.goto("https://www.educative.io/edpresso")

    search_box = await page.querySelector('.lg\:bg-gray-50 > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
    
    await search_box.type(keyword)
    await page.waitFor(4000)
    topics = await page.querySelectorAll("h2")
    new_topics = []
    for topic in range(len(topics)):
        title = await topics[topic].getProperty('textContent')
        title = await title.jsonValue()
        new_topics.append(title)

    return new_topics
    
async def get_tasks(keywords):
    tasks = []

    for keyword in keywords:
        task = await asyncio.create_task(fetch_data(keyword))
        tasks.append(tasks)

    return await asyncio.gather(*tasks)

async def main():
    global keywords

    output = await get_tasks(keywords)
    print(output)

asyncio.run(main())
