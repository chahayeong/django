from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test):
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        print(f'Train 의 type은 {type(this.train)} 이다.')
        print(f'Train 의 column 은 {this.test.columns} 이다.')
        print(f'Test 의 상위 5개 데이터는 {this.train} 이다.')
        print(f'Test 의 하위 5개 데이터는 {this.test.columns} 이다.')
        return this