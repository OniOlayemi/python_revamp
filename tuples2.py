#To really be sure that I am sure of what nemed tuple is

from collections import namedtuple

dict_files = dict(key1=100, key2=50, key3=140)
doct = {'x':23, 'yx':34}
#For a minute I forgot how to initialize a dictionary, initialize is not necessary though.
print(type(dict_files))
print(type(doct))

data = namedtuple('data', dict_files.keys())

data1 = data(**dict_files)

print(data1)

data2 = data(*dict_files.values())

print(data2)

print(data2._fields)

#what if a list is containing a dictionary
data_list = [{'key1':2, 'key2':34 }, {'key3':45, 'key4':32, 'key1':0}, {'key1':32, 'key2':11, 'key5':4, 'key4':45}]

keys_of = {key for dict_ in data_list for key in dict_}

print(keys_of)

tup_dict = namedtuple('tup_dict', sorted(keys_of))

print(tup_dict._fields)

tup_dict.__new__.__defaults__ = (None, ) * len(tup_dict._fields)
print(tup_dict)
tup_list = list(tup_dict(**dict_) for dict_ in data_list)

print(tup_list)

#I will run the codes over again to be sure that I really understand cause honestly,,, I mean...

ok_dict= {'key1':3, 'key2':3, 'key3':7, 'key4':9, 'key5':10, 'key6':33}

#now, I want to put this dictionary files into a named tuple, I think i should name the tuple first and keys
print('-'*12)
tup_ok = namedtuple('tup_ok', ok_dict.keys())
#gotta print to confirm, I am on the right path
print(tup_ok)
#nothing happened, I made a mistake though.

tup_ok1 = tup_ok(**ok_dict)
print(tup_ok1)

#maybe I should print the dict before adding it to any function, to check if I am on the right path
#the
#let's hit the list of dictionary

list_dict = [{'key1':1, "key2":8}, {'key3':2, 'key1':3, 'key4':12},{'key1':22, 'key2':10, 'key4':11, 'key5':3},{'key5':8}]

set_key = set(key for dict_ in list_dict for key in dict_.keys())
print(set_key)

tup_list = namedtuple('tup_list', sorted(set_key))

tup_list.__new__.__defaults__ = (None, ) * len(set_key)

print(tup_list())

#now, what is next? initializing a list of named tuples but how do I do that

tot_tup = [tup_list(**xx)for xx in list_dict]

print(tot_tup)


