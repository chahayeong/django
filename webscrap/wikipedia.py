class Wikipedia(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        while 1:
            menu = int(input('0.exit, 1.URL 입력, 2.URL 출력'))
            if menu == 0:
                break
            elif menu == 1:
                wiki = Wikipedia(input('URL 입력:'))
            elif menu == 2:
                print(f'URL 출력: {wiki}')

Wikipedia.main()
