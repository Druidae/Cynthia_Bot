import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


ua = UserAgent()



def get_page(categories):
    url = f'https://www.pepper.ru/groups/{categories}'
    result_json = {}

    # options
    options = webdriver.ChromeOptions()

    # user-agent
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=Service(executable_path="./chromedriver"),
        options=options
    )


    try:
        driver.get(url=url)

        SCROLL_PAUSE_TIME = 1.5
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            page = driver.find_element(By.ID, 'pagination').find_elements(By.CLASS_NAME, 'pagination-page')[-2].text.strip()
            if new_height == last_height and driver.find_element(By.ID, 'pagination').find_elements(By.CLASS_NAME, 'pagination-page')[-2].text.strip() != f'Страница 50':
                src = driver.page_source

                soup = BeautifulSoup(src, 'lxml')
                item_cards = soup.find_all('div', 'thread-clickRoot')
                for card in item_cards:
                    if card.find('span', 'cept-show-expired-threads') or not card.find('div', 'threadGrid-title').find('span', 'thread-price') or not card.find('a', 'thread-link') or not card.find('a', 'thread-link')['href']:
                        # print('[!] Error')
                        continue
                    item_name : str = card.find('a', 'thread-link').text.strip()
                    item_url : str = card.find('a', 'thread-link')['href'].strip()
                    item_id = item_url.split('-')[-1]
                    item_price :str = card.find('div', 'threadGrid-title').find('span', 'thread-price').text.strip()
                    
                    result_json[item_id] = {
                        'item_name': item_name,
                        'item_price': item_price,
                        'item_url': item_url,
                    }

                time.sleep(3)
                print(f'[+] Scraping {page} of 50')

                button = driver.find_element(By.ID, 'pagination').find_element(By.CLASS_NAME, 'cept-next-page').find_element(By.CLASS_NAME, 'button')
                button.click()
            elif new_height == last_height and driver.find_element(By.ID, 'pagination').find_elements(By.CLASS_NAME, 'pagination-page')[-2].text.strip() == f'Страница 50':
                src = driver.page_source

                soup = BeautifulSoup(src, 'lxml')
                item_cards = soup.find_all('div', 'thread-clickRoot')
                for card in item_cards:
                    if card.find('span', 'cept-show-expired-threads'):
                        # print('[!] Error')
                        continue
                    item_name = card.find('a', 'thread-link').text.strip()
                    item_url = card.find('a', 'thread-link')['href'].strip()
                    item_id = item_url.split('-')[-1]
                    item_price = card.find('span', 'thread-price').text.strip()
                    
                    result_json[item_id] = {
                        'item_name': item_name,
                        'item_price': item_price,
                        'item_url': item_url,
                    }
                print('[+] Finaly')
                break
            last_height = new_height
            time.sleep(2)
        
        with open(f'data/pepper_ru_scrap/output_data/{categories}_result.json', 'w') as file:
            json.dump(result_json, file, indent=4, ensure_ascii=False)


        # with open('data/test_data/index.html', 'w') as file:
        #     file.write(pagination_lists[-1])        
        # return pagination_lists
        

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def get_fresh_page(categories):
    fresh_items = {}

    with open(f'data/pepper_ru_scrap/output_data/{categories}_result.json', 'r') as file:
        new_dict = json.load(file)

    url = f'https://www.pepper.ru/groups/{categories}'
    result_json = {}

    options = webdriver.ChromeOptions()

    # user-agent
    options.add_argument(f"user-agent={ua.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.headless = True

    driver = webdriver.Chrome(
        service=Service(executable_path="./chromedriver"),
        options=options
    )

    try:
        driver.get(url=url)

        SCROLL_PAUSE_TIME = 1.5
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            page = driver.find_element(By.ID, 'pagination').find_elements(By.CLASS_NAME, 'pagination-page')[-2].text.strip()

            if new_height == last_height and driver.find_element(By.ID, 'pagination').find_elements(By.CLASS_NAME, 'pagination-page')[-2].text.strip() < f'Страница 1':
                src = driver.page_source

                soup = BeautifulSoup(src, 'lxml')
                item_cards = soup.find_all('div', 'thread-clickRoot')

                for card in item_cards:
                    if card.find('span', 'cept-show-expired-threads') or not card.find('div', 'threadGrid-title').find('span', 'thread-price') or not card.find('a', 'thread-link') or not card.find('a', 'thread-link')['href']:
                        # print('[!] Error')
                        continue

                    item_url : str = card.find('a', 'thread-link')['href'].strip()
                    item_id = item_url.split('-')[-1]

                    if item_id in new_dict:
                        continue
                    else:
                        item_name : str = card.find('a', 'thread-link').text.strip()
                        item_price :str = card.find('span', 'thread-price').text.strip()
                        
                        new_dict[item_id] = {
                            'item_name': item_name,
                            'item_price': item_price,
                            'item_url': item_url,
                        }

                        fresh_items[item_id] = {
                            'item_name': item_name,
                            'item_price': item_price,
                            'item_url': item_url,
                        }

                time.sleep(3)
                print(f'[+] Scraping {page} of 2')

                button = driver.find_element(By.ID, 'pagination').find_element(By.CLASS_NAME, 'cept-next-page')
                button.click()


            elif new_height == last_height and driver.find_element(By.ID, 'pagination').find_elements(By.CLASS_NAME, 'pagination-page')[-2].text.strip() >= f'Страница 1':
                src = driver.page_source

                soup = BeautifulSoup(src, 'lxml')
                item_cards = soup.find_all('div', 'thread-clickRoot')

                for card in item_cards:
                    if card.find('span', 'cept-show-expired-threads') or not card.find('div', 'threadGrid-title').find('span', 'thread-price') or not card.find('a', 'thread-link') or not card.find('a', 'thread-link')['href']:
                        # print('[!] Error')
                        continue

                    item_url : str = card.find('a', 'thread-link')['href'].strip()
                    item_id = item_url.split('-')[-1]

                    if item_id in new_dict:
                        continue
                    else:
                        item_name : str = card.find('a', 'thread-link').text.strip()
                        item_price :str = card.find('span', 'thread-price').text.strip()
                        
                        new_dict[item_id] = {
                            'item_name': item_name,
                            'item_price': item_price,
                            'item_url': item_url,
                        }

                        fresh_items[item_id] = {
                            'item_name': item_name,
                            'item_price': item_price,
                            'item_url': item_url,
                        }

                print('[+] Finaly')
                break
            last_height = new_height
            time.sleep(2)
        
        with open(f'data/pepper_ru_scrap/output_data/{categories}_result.json', 'w') as file:
            json.dump(new_dict, file, indent=4, ensure_ascii=False)

        return fresh_items

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def get_csv(categories):
    pass

def main():
    print(get_fresh_page(categories='laptop'))

if __name__ == '__main__':
    main()