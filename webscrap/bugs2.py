from bs4 import BeautifulSoup
import requests
import pandas as pd


class bugs2(object):
    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_list = []
    artist_list = []
    dict = {}
    df = pd.DataFrame()

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------- 제목 --------')
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[1]}))
        for i in ls:
            print(f' {i.find("a").text}')
            self.title_list.append(i.find("a").text)
        print('------ 가수 --------')
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls:
            print(f'{i.find("a").text}')
            self.artist_list.append(i.find("a").text)

    def insert_dict(self):
        ''' 같은방법
        for i in range(0, len(self.title_list)):
            self.dict[self.title_list[i]] = self.artist_list[i]
        '''
        for i, j in enumerate(self.title_list):
            self.dict[j] = self.artist_list[i]

    def to_frame(self):
        self.df = pd.DataFrame(self.dict, index=[0])
        print(self.df)

    def csv_save(self):
        path = './data/bucs.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

    def csv_read(self):
        self.df = pd.read_csv("bugs_racking.csv")
        print(self.df)

    @staticmethod
    def main():
        bugs = bugs2()
        while 1:
            menu = input('0-exit, 1-input time, 2-output, 3.dictionary, 4.data frame, 5.csv read')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url(input('상세정보 입력'))  # wl_ref=M_contents_03_01
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.insert_dict()
            elif menu == '4':
                bugs.csv_save()
            elif menu == '5':
                bugs.csv_read()
            else:
                print('Wrong Number')
                continue


bugs2.main()
