import time

from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
 
CHROMEDRIVER = "/usr/bin/chromedriver"
 

if __name__ == '__main__':
    start = time.time()
    url = "https://hole-golf.web.app/"
    options = Options()
    options.add_argument('--headless')
 
    driver = webdriver.Chrome(CHROMEDRIVER, options=options)
    pbar = tqdm(bar_format = "{n_fmt} [{elapsed}]")
    sec_5h45m = (60 * 5 + 45) * 60
    try:
        while time.time() - start < sec_5h45m:
            driver.get(url)
            
            title = driver.find_element(By.TAG_NAME, "h1")
            driver.refresh()
            pbar.update(1)
            time.sleep(0.5)
    except KeyboardInterrupt:
        driver.quit()