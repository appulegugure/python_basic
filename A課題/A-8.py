users_info = [["Bob", 79],
              ["Tom", 59],
              ["Ken", 61]]

print('\n'.join(["Name: {0}, Age: {1}".format(test[0], test[1]) for test in users_info]))
