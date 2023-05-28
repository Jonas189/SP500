import copy
import math

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

import wooldridge as woo

import pandas_datareader as pdr

import scipy.stats as stats


result1 = math.sqrt(16)
#print(result1)

result3 = math.e
#print(result3)

#l = np.array([1, 5, 41.3, 2.0])
#print (l)

var1 = ['Florian', 'Daniel']
var2 = [96, 49]
var3 = [True, False]
example_dict = dict(name=var1, points=var2, passed=var3)
#print(example_dict)

copied_dict = copy.deepcopy(example_dict)
copied_dict['points'][1] = 9
#print(example_dict)
#print(copied_dict)


#x = np.linspace(-3,3,20)
#plt.plot(x, x**3)
#plt.plot(x, x**4)
#plt.grid()

# plt.show()

icecream_sales = np.array([30, 40, 35, 130, 120, 60])
weather_coded = np.array([0, 1, 0, 1, 1, 0])
customers = np.array([2000, 2100, 1500, 8000, 7200, 2000])
df = pd.DataFrame({'icecream_sales': icecream_sales,
                   'weather_coded': weather_coded,
                   'customers': customers})



ourIndex = pd.date_range(start='04/2010', freq='M', periods=6)
df.set_index(ourIndex, inplace=True)

df['weather'] = pd.Categorical.from_codes(codes=df['weather_coded'],
                                          categories=['bad bad', 'good'])

#print(df)

wage1 = woo.dataWoo('wage1')
#print(wage1.head())



x = [1, 3, 4, 7, 8, 9]
y = [0, 3, 6, 9, 7, 8]
plt.plot(x, y)
plt.grid()
#plt.show()

affairs = woo.dataWoo('affairs')
affairs["ratemarr"] = affairs["ratemarr"] - 1
affairs["haskids"] = pd.Categorical.from_codes(affairs['kids'],
                                               categories=['no', 'yes'])
mlab = ['very unhappy', 'unhappy', 'average', 'happy', 'very happy']
affairs['marriage'] = pd.Categorical.from_codes(affairs['ratemarr'],
                                                categories=mlab)

counts = affairs['marriage'].value_counts()
counts_bykids = affairs['marriage'].groupby(affairs['haskids']).value_counts()
counts_yes = counts_bykids['yes']
counts_no = counts_bykids['no']

#print(counts, counts_bykids)

# pie chart (a):
#grey_colors = ['0.3', '0.4', '0.5', '0.6', '0.7']
#plt.pie(counts, labels=mlab)
#plt.savefig('PyGraphs/Descr-Pie.pdf')
#plt.close()
#plt.show()

ceosal1 = woo.dataWoo('ceosal1')

# extract roe:
roe = ceosal1['roe']

# subfigure a (histogram with counts):
plt.hist(roe, color='grey')
plt.ylabel('Counts')
plt.xlabel('roe')
plt.grid()
#plt.savefig('PyGraphs/Histogram1.pdf')
#plt.close()
#plt.show()

# pedestrian approach:
c = math.factorial(10) / (math.factorial(2) * math.factorial(10 - 2))
p1 = c * (0.2 ** 2) * (0.8 ** 8)
#print(f'p1: {p1}\n')

# scipy function:
p2 = stats.binom.pmf(2, 10, 0.2)
#print(f'p2: {p2}\n')



np.random.seed(123456)

# set sample size and MC simulations:
r = 10000
n = 100

# initialize arrays to later store results:
CIlower = np.empty(r)
CIupper = np.empty(r)
pvalue1 = np.empty(r)
pvalue2 = np.empty(r)

# repeat r times:
for j in range(r):
    # draw a sample:
    sample = stats.norm.rvs(10, 2, size=n)
    sample_mean = np.mean(sample)
    sample_sd = np.std(sample, ddof=1)
    # test the (correct) null hypothesis mu=10:
    testres1 = stats.ttest_1samp(sample, popmean=10)
    pvalue1[j] = testres1.pvalue
    cv = stats.t.ppf(0.975, df=n - 1)
    CIlower[j] = sample_mean - cv * sample_sd / np.sqrt(n)
    CIupper[j] = sample_mean + cv * sample_sd / np.sqrt(n)
    # test the (incorrect) null hypothesis mu=9.5 & store the p value:
    testres2 = stats.ttest_1samp(sample, popmean=9.5)
    pvalue2[j] = testres2.pvalue

plt.figure(figsize=(3, 5))  # set figure ratio
plt.ylim(0, 101)
plt.xlim(9, 11)
for j in range(1, 101):
    if 10 > CIlower[j] and 10 < CIupper[j]:
        plt.plot([CIlower[j], CIupper[j]], [j, j], linestyle='-', color='grey')
    else:
        plt.plot([CIlower[j], CIupper[j]], [j, j], linestyle='-', color='black')
plt.axvline(10, linestyle='--', color='black', linewidth=0.5)
plt.ylabel('Sample No.')
plt.show()