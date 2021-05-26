class VectorTest(object):
    ls = ['abcd', 786, 2.23, 'john', 70.2]
    tinyls = [123, 'john']
    tp = ('abcd', 786, 2.23, 'john', 70.2)
    tinytp = (123, 'john')
    dt = {'abcd': 786, 'john': 70.2}
    tinydt = {'홍': 30}

    def list_create(self, lsadd):
        self.ls.append(lsadd)
        print(self.ls)

    def list_read(self):
        for i in self.ls:
            print(i)

    def list_update(self):
        ls2 = self.ls + self.tinyls
        print(ls2)

    def list_delete(self, lsdel):
        self.ls.remove(lsdel)
        print(self.ls)

    def Tuple_create(self, tpadd):
        tplist = list(self.tp)
        tplist.append(tpadd)
        self.tp = tuple(tplist)
        print(self.tp)

    def Tuple_read(self):
        for i in self.tp:
            print(i)

    def Tuple_uerch(self):
        tp2 = self.tp + self.tinytp
        print(tp2)

    def Tuple_delete(self, tpdel):
        tplist = list(self.tp)
        tplist.remove(tpdel)
        self.tp = tuple(tplist)
        print(self.tp)

    def Dictionary_create(self, addkey, addvalue):
        self.dt[addkey] = addvalue
        print(self.dt)

    def Dictionary_read(self):
        for i in self.dt:
            print(i)

    def Dictionary_update(self):
        self.dt.update(self.tinydt)
        print(self.dt)

    def Dictionary_delete(self, delkey):
        del self.dt[delkey]
        print(self.dt)

    @staticmethod
    def main():
        v = VectorTest()

        while 1:
            menu = int(input('-------------------------------------------------0.exit\n'
                             '<List> 1.Ctreate, 2.Read, 3.Update, 4.Delete\n'
                             '<Tuple> 5.Ctreate, 6.Read, 7.Update, 8.Delete\n'
                             '<Dictionary> 9.Ctreate, 10.Read, 11.Update, 12.Delete\n'))

            if menu == 0:
                break
            elif menu == 1:
                v.list_create(input('추가할 값을 쓰세요:'))
            elif menu == 2:
                v.list_read()
            elif menu == 3:
                v.list_update()
            elif menu == 4:
                v.list_delete(input('삭제할 값을 쓰세요:'))
            elif menu == 5:
                v.Tuple_create(input('추가할 값을 쓰세요:'))
            elif menu == 6:
                v.Tuple_read()
            elif menu == 7:
                v.Tuple_murch()
            elif menu == 8:
                v.Tuple_delete(input('삭제할 값을 쓰세요:'))
            elif menu == 9:
                v.Dictionary_create(input('추가할 키값을 쓰세요:'), input('추가할 값을 쓰세요'))
            elif menu == 10:
                v.Dictionary_read()
            elif menu == 11:
                v.Dictionary_update()
            elif menu == 12:
                v.Dictionary_delete(input('삭제할 키를 쓰세요:'))
            else:
                continue


VectorTest.main()