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


###########################
# CHAPTER  - 6            #
# Probability             #
###########################


from collections import Counter
import math, random

# Normal Distribution
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

def plot_normal_pdfs(plt):
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
    plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
    plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
    plt.plot(xs,[normal_pdf(x,mu=-1)   for x in xs],'-.',label='mu=-1,sigma=1')
    plt.legend()
    plt.show()

#plot_normal_pdfs(plt)          #call normal distribution

# Central Limitation

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(p, n):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p, n, num_points):
    
    data = [binomial(p, n) for _ in range(num_points)]
    
    # use a bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')
    
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # use a line chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) 
          for i in xs]
    plt.plot(xs,ys)
    plt.show()

#make_hist(0.75, 100, 10000)

###########################
# CHAPTER  - 8            #
# Gradient Descent        #
###########################


#from linear_algebra import distance, vector_subtract, scalar_multiply
#import linear_algebra
import math, random

def sum_of_squares(v):
    """computes the sum of squared elements in v"""
    return sum(v_i ** 2 for v_i in v)

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def plot_estimated_derivative():

    def square(x):
        return x * x

    def derivative(x):
        return 2 * x

    derivative_estimate = lambda x: difference_quotient(square, x, h=0.00001)

    # plot to show they're basically the same
    import matplotlib.pyplot as plt
    x = range(-10,10)
    plt.plot(x, map(derivative, x), 'rx')           # red  x
    plt.plot(x, map(derivative_estimate, x), 'b+')  # blue +
    plt.show()                                      # purple *, hopefully

#plot_estimated_derivative()


###########################
# CHAPTER  - 9            #
# Getting Data            #
###########################

# egrep.py
import sys, re

if __name__ == "__main__":     

    # sys.argv is the list of command-line arguments
    # sys.argv[0] is the name of the program itself
    # sys.argv[1] will be the regex specfied at the command line
    
    regex = sys.argv[1]
    
    cnt1 =0
    # for every line passed into the script
    for line in sys.stdin:
        # if it matches the regex, write it to stdout
        if re.search(regex, line):
            cnt1 +=1
            sys.stdout.write(str(cnt)+'--'+line )  # or use line[:10] to list begin 10 words
## How to use egrep.py , to compare sys.argv[1] match any line content of **.txt
            #then list its line 
## typing below in WIN cmd line,             
## type SomeFile.txt | python egrep.py "[0-9]" | python line_count.py
            

# most_common_words.py
import sys
from collections import Counter

if __name__ == "__main__":

    # pass in number of words as first argument
    try:
        num_words = int(sys.argv[1])
    except:
        print "usage: most_common_words.py num_words"
        sys.exit(1)   # non-zero exit code indicates error

    counter = Counter(word.lower()               #Counter(), same word with its counts
                      for line in sys.stdin             
                      for word in line.strip().split()  
                      if word)                          
            
    for word, count in counter.most_common(num_words):  # choice "num_words" most common  
        sys.stdout.write(str(count))
        sys.stdout.write("\t")
        sys.stdout.write(word)
        sys.stdout.write("\n")
## How to use most_common_words.py , to count sys.argv[1] most word each line of **.txt
            #then list its most words-- counter 
## typing below in WIN cmd line,             
## type the_bible.txt | python most_common_words.py 10


#re_data.py  <- read write file by open
cnt_hash = 0

with open('test_script.txt','r') as f:    #use 'with" , can skip close file
    for line in f:
        if re.match("wriu",line):
            cnt_hash +=1
print cnt_hash

def get_split_space(cntx):
    return cntx.lower().split("-w")   # [x] split times by "-w", [-1]:all

with open('test_script.txt','r') as f:
    script_cnt = Counter(get_split_space(line)[0]   #[0]:fist of extraction
                         for line in f
                         if "wriu" in line)
print script_cnt.items()



#Scrapping the Web
#need to install html5, bs4 by "pip install bs4 (or html5lib)"
from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.google.com").text
soup = BeautifulSoup(html, 'html5lib')
#print soup



