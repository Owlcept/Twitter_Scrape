#Playwright playground
from playwright.sync_api import sync_playwright, ViewportSize

with sync_playwright() as p:
    browser = p.firefox.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://twitter.com/domiono/status/1538891392583450629')
 
    #This was pure testing, will be removed in final
    page.locator('data-testid=tweet').screenshot(path="twitter_scrape/title.png")
    x = page.locator('data-testid=tweet')
    y = page.locator('data-testid=tweetText')
    print(x.count())
    for i in range(1,9):
        #This colects the text(does not grab emoji
        print(y.nth(i).text_content())
        x.nth(i).screenshot(path = f'./twitter_scrape/title{i}.png')
    browser.close()

