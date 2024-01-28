import statistics
# First dictionary
my_dict1 = {}
my_dict1[('A', 'B')] = 100
my_dict1[('A', 'C')] = 100
my_dict1[('B', 'C')] = 300

# Second dictionary
my_dict2 = {}
my_dict2[('A', 'B')] = 100
my_dict2[('A', 'C')] = 140
my_dict2[('B', 'C')] = 100


# Third dictionary
my_dict3 = {}
my_dict3[('A', 'B')] = 100
my_dict3[('A', 'C')] = 120
my_dict3[('B', 'C')] = 100


# List of dictionaries
list_of_dicts = [my_dict1, my_dict2, my_dict3]


a=[1]

print(statistics.stdev(a))
     


