import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


class naver_Movie(object):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = ''
    title_list = []
    df = pd.DataFrame()
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {"class": 'tit3'})
        for i in all_div:
            self.title_list.append(i.find("a").text)

        # print(self.title_list)
        driver.close()

    def li_to_dataframe(self):
        self.df = pd.DataFrame({'영화제목': self.title_list})
        # print(self.df)

    def csv_save(self):
        path = './data/movie_rank.csv'
        self.df.to_csv(path, na_rep='NaN')


if __name__ == '__main__':
    nm = naver_Movie()
    # tit3
    nm.scrap()
    nm.li_to_dataframe()
    nm.csv_save()

