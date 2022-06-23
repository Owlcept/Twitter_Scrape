#Created by: Owlcept
from playwright.sync_api import sync_playwright

def twitter_scrape(tweet, num_com=9):

    with sync_playwright() as p:
        #Must use firefox // Other chromium wont load tweets
        browser = p.firefox.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(tweet)

        #Debug tweet below
        #page.goto('https://twitter.com/domiono/status/1538891392583450629')
    
        #Title Screenshot
        page.locator('data-testid=tweet').screenshot(path="Twitter_Scrape/assets/title.png")
        x = page.locator('data-testid=tweet')
        y = page.locator('data-testid=tweetText')
    
        #Use 1 as start for skipping title
        for i in range(1,num_com):
            if i==3:
                #Skip the 3rd screenshot because of signup banner
                continue
            #This colects the text(does not grab emoji

            print(y.nth(i).text_content())
            x.nth(i).screenshot(path = f'Twitter_Scrape/assets/title{i}.png')
        browser.close()

