from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup 
from pprint import pprint
from time import sleep

def convert_num(detail_list):
    '''convert K, M numbers to integer values'''
    print(detail_list[2])
    if "K" in detail_list[2]:
        tweet_count  =  (int(detail_list[2].replace("K", "")))*1000
        return tweet_count
    
    elif "M" in detail_list[2]:
        (int(detail_list[2].replace("M", "")))*1000
        tweet_count = int(detail_list[2])
        return tweet_count
    
    else:
        tweet_count = detail_list[2]
        return tweet_count
def run(playwright):
    '''Execute script to scrape trending word data from trends24 filtered to United-States'''
    # -----------launch and setup browser/webpage
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page() 
    
    #-----------------Block Ads
    page.route("**/*", lambda route, request: (
        route.abort()
        if any(ad in request.url for ad in ["ads", "doubleclick", "googlesyndication", "googletagmanager", "adservice", "analytics", "popads"])
        else route.continue_()
    ))
    # -------------load site to scrape
    page.goto("https://trends24.in/united-states/", wait_until="domcontentloaded")

    #--------------Get the <ol> elements that holds the 1-hour trends
    content_element = page.locator('//*[@id="timeline-container"]/div[1]/div[1]/ol').first
    ol_html = content_element.inner_html()  # Get HTML inside <ol>

    
    # -------Create webpage BS4 instance
    soup = BeautifulSoup(ol_html, 'html.parser')  # Parse the inner HTML

    #-------Extract list items
    items = soup.select("li span a")
    trends = [item.get_text(strip=True) for item in items]

    # -------------trend full data
    trend_list = []
    # ----------simulating clicks to go into inner page for detailed scrape
    sub_trend = trends[:5]
    for trend in sub_trend:    
        page.get_by_text(trend).first.click() #-------locate trend link by word

        detail_content = page.locator('//*[@id="trendcheck-dialog"]/div[2]/div[1]') #------------locate Xpath of detail container
        inner_html = detail_content.inner_html() #------extract inner html of container
        inner_soup =  BeautifulSoup(inner_html, 'html.parser')  #------- Parse the inner HTML with BS4
        detail = inner_soup.select("dl div dd")
        detail_list = [det.get_text(strip=True) for det in detail] #-------Extract text from html
        tweet_count = convert_num(detail_list)
        

        rank  = int(detail_list[0])
        trend_time = detail_list[3] 
        details = {
            "trend": trend,
            "rank":rank, 
            "trendtime":trend_time, 
            "tweetcount":tweet_count
        }
        trend_list.append(details)
        pprint(details)
        
        page.get_by_role("button", name="Close popup").click()
    # pprint(trend_list)
    browser.close()
with sync_playwright() as playwright:
    run(playwright)



