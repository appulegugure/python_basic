bob_info = {"first_name": "Bob", "family_name": "Dylan", "age": 79}
print('\n'.join(str(i) + ":" + str(bob_info[i]) for i in bob_info.keys()))

"""
print(bob_info["first_name"])
print(bob_info["family_name"])
print(bob_info["age"])
"""
