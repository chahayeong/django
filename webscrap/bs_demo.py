from bs4 import BeautifulSoup
class BsDemo(object):

    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        bs = BsDemo()
        while 1:
            menu = int(input('0.exit, 1.URL 입력, 2.URL 출력, 3.타이틀 출력'))

            if menu == 0:
                break
            elif menu == 1:
                bs.url = """<html><head><title>The Dormouse's story</title></head>
                                    <body>
                                    <p class="title"><b>The Dormouse's story</b></p>

                                    <p class="story">Once upon a time there were three little sisters; and their names were
                                    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                                    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                                    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                                    and they lived at the bottom of a well.</p>

                                    <p class="story">...</p>"""
            elif menu == 2:
                soup = BeautifulSoup(bs.url, 'html.parser')
                print(soup.prettify())
            elif menu == 3:
                soup = BeautifulSoup(bs.url, 'html.parser')
                print(soup.p['class'])
            else:
                print('wrong number')
                continue


BsDemo.main()
