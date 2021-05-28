from bs4 import BeautifulSoup
import requests


class melon2(object):
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------- 제목 --------')
        ls = soup.find_all("div", {"class": self.class_name[0]})
        for i in ls:
            print(f' {i.find("a").text}')
        print('------ 가수 --------')
        ls = soup.find_all("div", {"class": self.class_name[1]})
        for i in ls:
            print(f' {i.find("a").text}')

    def to_dictionary(self):
        for i in range(0, len(self.title_ls)):
            pass

    @staticmethod
    def main():
        melon = melon2()
        while 1:
            menu = input('0-exit, 1-input time, 2-output, 3-data dictionary  4-data frame, 5.read csv')
            if menu == '0':
                break
            elif menu == '1':
                melon.set_url(input('스크래핑할 날짜 입력'))  # '2021052511'
            elif menu == '2':
                melon.class_name.append('ellipsis rank01')
                melon.class_name.append('ellipsis rank02')
                melon.get_ranking()
            elif menu == '3':
                pass
            elif menu == '4':
                pass
            else:
                print('Wrong number')
                continue


melon2.main()