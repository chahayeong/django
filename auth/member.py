class Member(object):

    nid = ''
    password = ''
    name = ''
    email = ''

    def join(self):
        pass

    def login(self):
        pass

    def mypage(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass

    @staticmethod
    def main():
        m = Member()
        while 1:
            menu = int(input('0.exit, 1.회원가입, 2.로그인, 3.내정보, 4.회원수정, 5.회원탈퇴'))

            if menu == 0:
                break
            elif menu == 1:
                m.nid = input('사용할 id:')
                m.password = input('사용할 password:')
                m.name = input('사용자 이름:')
                m.email = input('사용자 이메일:')

            elif menu == 2:
                rogin_id = input('id입력:')
                rogin_password = input('password입력:')

                if m.nid == rogin_id and m.password == rogin_password:
                    print('로그인 되었습니다')
                else:
                    print('회원가입 정보가 없습니다')

            elif menu == 3:
                print(f'사용자 id: {m.nid}, 사용자 password: {m.password}, 사용자 이름: {m.name}, 사용자 이메일:{m.email}')

            elif menu == 4:
                pass

            elif menu == 5:
                pass

            else:
                continue


Member.main()
