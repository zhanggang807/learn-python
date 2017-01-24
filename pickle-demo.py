import pickle

a_dict = {'name' : 'admin'}

file = open('pickle-demo.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()

file = open('pickle-demo.pickle', 'rb')
dict1 = pickle.load(file)

print(a_dict)
print(dict1)
