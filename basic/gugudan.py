'''
구구단 프로그램은 단을 입력받아서, 입력받은 단의 1~9의 곱을 출력하는 어플이다.
단, 단은 정수이다
'''


class Gugudan(object):
    dan = 0
    dic = {}

    def calc(self):
        for i in range(1, 10):
            print(f'{self.dan}*{i}={self.dan * i}')

    def allcalc(self):
        for i in range(2, 10):
            for j in range(1, 10):
                print(f'{i}*{j}={i * j}')

    def print_dict_dan(self):
        for i in range(1, 10):
            self.dic[i] = self.dan * i
            print('딕셔너리 출력')
            print(self.dic)
            for k in self.dic.keys():
                print(f'{self.dan} * {k} = {self.dic.get(k)}')


    @staticmethod
    def main():
        g = Gugudan()

        while 1:
            menu = int(input('0.exit, 1.gugudan, 2.all dan, 3.with dict'))

            if menu == 0:
                break
            elif menu == 1:
                g.dan = int(input('단을 입력하세요:'))
                g.calc()
            elif menu == 2:
                    g.allcalc()
            elif menu == 3:
                g.dan = int(input('단 입력:'))
                g.print_dict_dan()


Gugudan.main()
