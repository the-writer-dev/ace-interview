example = {'key1': 'value1', 'key2': {'value2-1', 'value2-2'}}

# difference between del vs pop
# del does not return any value
# pop does return pop value

print(example)
value1 = example.pop('key1')
del example['key2']

print(example)

if example:
    print("hello")

