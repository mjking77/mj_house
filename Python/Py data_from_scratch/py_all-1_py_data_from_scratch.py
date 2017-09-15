###########################
# CHAPTER 1 -             #
# SALARIES AND EXPERIENCE #
###########################
# Arithmetic , 5/2=2 to 5/2=2.5 with floating as new-style division
from __future__ import division

from collections import defaultdict
from matplotlib import pyplot as plt
import numpy as np

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

def make_chart_salaries_by_tenure():
    tenures = [tenure for salary, tenure in salaries_and_tenures]
    salaries = [salary for salary, tenure in salaries_and_tenures]
    plt.scatter(tenures, salaries)
    plt.xlabel("Years Experience")
    plt.ylabel("Salary")
    plt.show()


# keys are sorting by years
# values are the ave salaries for each tenure group

def tenure_bucket(tenure):
    if tenure < 2: return "less than two"
    elif tenure < 5: return "between two and five"
    else: return "more than five"
# dict + append[list] , mj2017
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket1 = {
  tenure_bucket : sum(salaries) / len(salaries)
  for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
}


###########################
# CHAPTER 2 -             #
# Crash for Python        #
###########################

from collections import defaultdict

# BASIC data structure of Python
# List = [] , Tuple = () , Dictionary = {} ... tuple can't be append.
# usage of "defaultdict

dd_list = defaultdict(list)             # list() produces an empty list
dd_list["a"].append(0)                  # add one item at a time, contains {a: [0]}
dd_list["a"].extend([2,3])              # add [x,y,z..] use extend() {'a': [0, 2, 3])
dd_list[6].append(5)                    # = {'a': [0, 2, 3], 6: [5]})
dd_dict = defaultdict(dict)             # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"     # { "Joel" : { "City" : Seattle"}}
dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                       # now dd_pair contains {2: [0,1]}

# Sorting
x1 = [4,1,2,3]
y1 = sorted(x1)     # is [1,2,3,4], x is unchanged
x1.sort()          # now x is [1,2,3,4]
x2 = sorted([-4,1,-2,3], key=abs, reverse=True)  # is [-4,3,-2,1]

# List Comprehension
even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
even_squares = [x * x for x in even_numbers]        # [0, 4, 16]
square_dict = { x : x * x for x in range(5) }  # { 0:0, 1:1, 2:4, 3:9, 4:16 }
pairs = [(x, y)
         for x in range(1,5,1)
         for y in range(x+2)]   # 100 pairs (0,0) (0,1) ... (9,8), (9,9)

# random()
import random
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)  # [x, y, z, a, b, c]
four_with_replacement = [random.choice(range(10))
                         for _ in range(4)]          # [x, y, z, a]

# zip and Argument uppacking
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)        # is [('a', 1), ('b', 2), ('c', 3)]
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
zip(('a', 1), ('b', 2), ('c', 3))   #  [('a','b','c'), (1, 2, 3)]

# Object-Oriented Programming .. ? p60


###########################
# CHAPTER  - 5            #
# Statistics              #
###########################
import math as math

def mean(x):
    return sum(x) / len(x)

def sum_of_squares(v):
    """computes the sum of squared elements in v"""
    return sum(v_i ** 2 for v_i in v)

# Dispersion of variance  => standard deviation

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

# standard deviation => population / n ; sample / (n-1) 
def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n-1)

def standard_deviation(x):
    return math.sqrt(variance(x))

# numpy np.std ( x , ddot = y )  y=1 is sample sd
