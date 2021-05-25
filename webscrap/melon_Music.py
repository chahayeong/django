import urllib.request
from bs4 import BeautifulSoup


class melon_Music(object):

    url = ''
    hdr = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={time}'

    def set_class_name(self, class_name):
        self.class_name = class_name

    def get_ranking(self):
        req = urllib.request.Request(self.url, headers=self.hdr)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')

        print('-----제목-----')
        ls = soup.find_all("div", {"class": self.class_name[0]})
        for i in ls:
            print(f' {i.find("a").text}')
        print('-----가수-----')
        ls = soup.find_all("div", {"class": self.class_name[1]})
        for i in ls:
            print(f' {i.find("a").text}')

    @staticmethod
    def main():
        m = melon_Music()

        while 1:
            menu = int(input('0.exit, 1.url 입력, 2.ranking 출력'))

            if menu == 0:
                break
            elif menu == 1:
                m.set_url('2021052511')
            elif menu == 2:
                m.class_name.append('ellipsis rank01')
                m.class_name.append('ellipsis rank02')
                m.get_ranking()
            else:
                continue


melon_Music.main()
