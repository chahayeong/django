import pandas as pd

class Conversion(object):

    @staticmethod
    def tuple_produce() -> ():  # ->return값은 튜플()
        return 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    @staticmethod
    def tuple_list(t):
        return list(t)

    @staticmethod
    def list_float(ls):
        return [float(ls[i]) for i in range(9)]

    @staticmethod
    def list_int(ls):
        return list(map(int, ls))

    @staticmethod
    def list_dictionary(ls):
        return {str(i): ls[i] for i in range(len(ls))}

    @staticmethod
    def hello_tuple():
        return tuple('hello')

    @staticmethod
    def tup_list(t):
        return list(t)

    @staticmethod
    def dic_dp(d):
        return pd.DataFrame(d, index=[0])

    @staticmethod
    def main():
        c = Conversion()
        i = 0
        f = 0.0
        s = ''
        ls = []
        t = ()
        d = {}
        df = pd.DataFrame({})

        while 1:
            menu = int(input('0.exit'))

            if menu == 0:
                break
            elif menu == 1:  # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
                t = c.tuple_produce()
                print(t)
            elif menu == 2:  # 1번 튜플을 리스트로 전환하시오 (return)
                ls = c.tuple_list(t)
                print(ls)
            elif menu == 3:  # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
                ls = c.list_float(ls)
                print(ls)
            elif menu == 4:  # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
                ls = c.list_int(ls)
                print(ls)
            elif menu == 5:  # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오
                d = c.list_dictionary(ls)
                print(d)
            elif menu == 6:  # 'hello' 를 튜플로 전환하시오
                t = c.hello_tuple()
                print(t)
            elif menu == 7:  # 6번 튜플을 리스트로 전환하시오
                ls = c.tup_list(t)
                print(ls)
            elif menu == 8:  # 5번 딕셔너리를 데이터프레임으로 전환하시오
                df = c.dic_dp(d)
                print(df)
            else:
                continue


Conversion.main()
