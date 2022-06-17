#Playwright playground
import time
from playwright.sync_api import sync_playwright, ViewportSize

with sync_playwright() as p:
    browser = p.firefox.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://twitter.com/ardentreflexion/status/1537471416467177474')
    #                                                     1537501373100589056
    page.locator('data-testid=tweet').screenshot(path="./title.png")
    x = page.locator('data-testid=tweet')
    y = page.locator('data-testid=tweetText')
    print(x.count())
    for i in range(x.count()):
        print(y.nth(i).text_content())
        x.nth(i).screenshot(path = f'./title{i}.png')
    browser.close()

