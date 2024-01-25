import re
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium_stealth import stealth

from operational_units.rotating_proxies import check_proxies


class BaseScraper:
    def __init__(self):
        self.proxy = check_proxies()

    def get_webdriver(self):
        use_proxy = self.proxy
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--headless")
        options.add_argument("--enable-javascript")
        options.add_argument(f"--use-proxy={use_proxy}")
        options.add_experimental_option('useAutomationExtension', False)

        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        options.add_argument(f'--user-agent={user_agent}')
        driver = webdriver.Chrome(options=options)

        # Selenium Stealth settings
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        return driver

    def return_soup(self, url):
        driver = self.get_webdriver()
        driver.get(url)

        page_source = driver.execute_script('return document.documentElement.outerHTML')
        driver.quit()

        soup = BeautifulSoup(page_source, 'html.parser')
        return soup


if __name__ == '__main__':
    start = time.time()
    scraper = BaseScraper()

    end = time.time()
    print(str(end - start) + " s")
