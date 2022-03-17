from TransactionManager import TransactionManager

tm = TransactionManager()
result = True

while result:
    result = tm.get_new_transaction()
