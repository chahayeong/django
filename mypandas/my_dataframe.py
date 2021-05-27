class MyDataFrame(object):

    def __int__(self, columns, index):
        self.columns = columns
        self.index = index

    @staticmethod
    def main():
        df = MyDataFrame(10,3)