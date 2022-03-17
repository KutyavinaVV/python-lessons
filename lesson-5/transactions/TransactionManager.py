from functools import reduce
from InvalidTransactionException import InvalidTransactionException
import pickle
import os

DB_NAME = 'db.pkl'
QUIT_STRING = 'quit'


class TransactionManager:

    def __init__(self):
        super().__init__()
        self.__transactions_store = self.load_from_file()

    def load_from_file(self):
        if os.path.getsize(DB_NAME) > 0:
            file = open(DB_NAME, 'rb')
            res = pickle.load(file)
            file.close()
            return res
        return []

    def get_new_transaction(self):
        data = input()
        if data.__eq__(QUIT_STRING):
            self.write_result()
            return False

        self.write_new_transaction(data)
        return True

    def write_new_transaction(self, user_data):
        data = user_data.split(' ')
        if data.__len__() != 2:
            raise InvalidTransactionException('Invalid data, try it again')

        if not data[1].isdigit:
            raise InvalidTransactionException('Invalid data, try it again')

        new_transaction = {
            'name': data[0],
            'count': int(data[1])
        }
        self.__transactions_store.append(new_transaction)

    def write_result(self):
        unique_types = []

        for x in self.__transactions_store:
            if x['name'] not in unique_types:
                unique_types.append(x['name'])

        print("All types:", unique_types)

        for type in unique_types:
            filtered_transactions = list(filter(lambda t: t['name'] == type, self.__transactions_store))
            type_result = reduce(lambda t, y: y['count'] + t, filtered_transactions, 0)

            print(type, ": ", type_result)

        total_result = reduce(lambda t, y: y['count'] + t, self.__transactions_store, 0)
        print("Total count:", ": ", total_result)
        self.save_in_file()

    def save_in_file(self):
        file = open(DB_NAME, 'wb')
        pickle.dump(self.__transactions_store, file)
        file.close()
