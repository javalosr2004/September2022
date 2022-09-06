from pyppeteer import launch
import asyncio
from typing import List


async def launch_browser(browser, keyword):
    keyDict = {keyword : []}
   #browser = await launch(headless = True, executablePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', autoClose = False)
    page = await browser.newPage()
    await page.goto('https://www.educative.io/answers')
    #get search box
    search_box = await page.querySelector('.lg\:bg-gray-50 > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)')

    #type out keyword
    await search_box.type(keyword)
    await page.waitFor(4000)
    #find the titles
    titles = await page.querySelectorAll('h2')
    
    

    #extract titles
    for title in titles:
        text = title.getProperty('textContent')
        text = title.jsonValue()
        if text != 'Your Privacy':
            keyDict[keyword].append(text)
    
    #put it into a dictionary
    return keyDict
    
async def output_data(data_list):
    for dict in data_list:
        for keyword, data in dict.items():
            print(f'================{keyword}================')
            for title in data:
                print(title)
            print('\n\n')

async def main(keywords: List[str]):
    tasks = []
    browser = await launch(headless = True, executablePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', autoClose = False)

    for keyword in keywords:
        task = launch_browser(browser, keyword)
        tasks.append(task)
    
    output = await asyncio.gather(*tasks)

    await browser.close()

    for dict in output:
        for keyword, data in dict.items():
            print(f'================{keyword}================')
            for title in data:
                print(title)
            print('\n\n')
    

asyncio.run(main(['python', 'virtual']))