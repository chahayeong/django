import pandas as pd

class Conversion(object):
    i = 0
    f = 0.0
    s = ''
    ls = []
    t = ()
    d = {}
    df = pd.DataFrame({})

    def tuple_produce(self):
        self.t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        return self.t

    def tuple_list(self):
        self.ls = list(self.t)
        return self.ls

    def list_float(self):  # 원래는 아래 함수 사용
        for i in range(0, 10):
            self.ls[i] = float(self.ls[i])
        return self.ls

    def list_int(self):
        self.ls = list(map(int, self.ls))
        return self.ls

    def list_dictionary(self):
        self.d = {str(i): self.ls[i] for i in range(len(self.ls))}
        return self.d

    def hello_tuple(self):
        self.t = tuple('hello')
        return self.t

    def tup_list(self):
        self.ls = list(self.t)
        return self.ls

    def dic_dp(self):
        self.df = pd.DataFrame(self.d, index=[0])
        return self.df

    @staticmethod
    def main():
        c = Conversion()

        while 1:
            menu = int(input('0.exit'))

            if menu == 0:
                break
            elif menu == 1:  # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
                print(c.tuple_produce())
            elif menu == 2:  # 1번 튜플을 리스트로 전환하시오 (return)
                print(c.tuple_list())
            elif menu == 3:  # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
                print(c.list_float())
            elif menu == 4:  # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
                print(c.list_int())
            elif menu == 5:  # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오
                print(c.list_dictionary())
            elif menu == 6:  # 'hello' 를 튜플로 전환하시오
                print(c.hello_tuple())
            elif menu == 7:  # 6번 튜플을 리스트로 전환하시오
                print(c.tup_list())
            elif menu == 8:  # 5번 딕셔너리를 데이터프레임으로 전환하시오
                print(c.dic_dp())
            else:
                continue


Conversion.main()
