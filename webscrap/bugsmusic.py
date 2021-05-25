from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):
    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def ranking(url, category):
        print(f'URL 출력: {url}')
        soup = BeautifulSoup(urlopen(url), 'lxml')
        cate = category.lower()

        print(f'------------{cate.upper()} RANKING------------')
        n_category = 0
        for link1 in soup.find_all(name='p', attrs=({"class": f"{cate}"})):
            n_category += 1
            print(f'{str(n_category)} RANKING')
            print(f'{cate}: {link1.find("a").text}')

    # https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = int(input('0.exit, 1.URL 입력, 2.음악순위'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('URL 입력: ')

            elif menu == 2:
                bugs.ranking(bugs.url, str(input('검색할 랭킹항목: ')))
            else:
                print('wrong number')
                continue


BugsMusic.main()
