from django.core.management.base import BaseCommand
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import warnings
warnings.simplefilter('ignore')

from scraping.models import CompanyInfo

def get_company_data():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome("./chromedriver", options=options)

    driver.implicitly_wait(10)
    url = "https://job.mynavi.jp/24/pc/search/query.html?OP:12/"
    time.sleep(5)
    driver.get(url)

    cols=['会社名', "従業員" ]
    df = pd.DataFrame(index=[], columns=cols)
    i = 1
    while True:
        try:
            is_data = driver.find_elements(By.CLASS_NAME,"boxSearchresultEach")
            for data in is_data:
                company_name = data.find_element(By.CSS_SELECTOR,"h3").text                
                people_num= data.find_element(By.CLASS_NAME, 'linkCtg')
                num = people_num.text.find("従業員")
                people_num = people_num.text
                people_num = people_num[num:]

                df = df.append({"会社名":company_name, "従業員": people_num}, ignore_index=True)

            next_page = driver.find_element(By.ID,"lowerNextPage")
            next_page.click()
            
            print(i, "ページ読み込み済み")
            i += 1        
            
            if i == 2:
                break
            
        except:
            driver.quit()
            break
        
    return df
        
# if __name__ == "__main__":
#     df = get_compan_data()
#     print(df)

    
class Command(BaseCommand):
    
    help = "mynaviから会社名と従業員数をスクレイピングしてDBへ保存"
    
    def handle(self, *args, **options):
        df = get_company_data()
        print("カスタムコマンドを実行")
        
        for data in df.itertuples(name = None):
            company_data = CompanyInfo(name = data[1], people_num = data[2])
            try:
                company_data.save()
            except:
                print("エラー")