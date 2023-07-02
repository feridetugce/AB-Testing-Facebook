import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
import statsmodels.stats.proportion as proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Assinging name for dataframes
control = pd.read_excel("ab_testing.xlsx", sheet_name="Control Group")
test = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")

# Analyze the dataframes 
control.describe().T
test.describe().T

df = pd.concat([control, test], axis=0, ignore_index=True )
df.head()


# H0 : There is no statistically significant difference between the Control group that was served “maximum bidding” campaign and Test group that was served “average bidding” campaign.
# H1 : There is statistically significant difference between the Control group that was served “maximum bidding” campaign and Test group that was served “average bidding” campaign.


control["Purchase"].mean()
test["Purchase"].mean()

############ Hyphotesis Testing ###############

# Indepented Two Sample T-Test
# The Independent Samples t Test compares the means of two independent groups in order to determine whether there is statistical evidence that the associated population means are significantly different.

# Requirements
# Normal distribution: Non-normal population distributions, especially those that are thick-tailed or heavily skewed, considerably reduce the power of the test
# Homogeneity of variances : When this assumption is violated and the sample sizes for each group differ, the p value is not trustworthy.

# The null hypothesis (H0) and alternative hypothesis (H1) of the Independent Samples t Test can be expressed in two different but equivalent ways:

# H0: µ1 = µ2 (the two population means are equal)
# H1: µ1 ≠ µ2 (the two population means are not equal)
 
# The Shapiro-Wilks Test for Normality

# H0: There is no statistically significant difference between sample distribution and theoretical normal distribution
# H1: There is statistically significant difference between sample distribution and theoretical normal distribution

# The test rejects the hypothesis of normality when the p-value is less than or equal to 0.05. Failing the normality test allows you to state with 95% confidence the data does not fit the normal distribution.

p-value < 0.05 (H0 rejected)
p-value > 0.05 (H0 not rejected)

test_stat, pvalue = shapiro(test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

                                # p-value=0.1541 > 0.05 do not reject
                          

test_stat, pvalue = shapiro(control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

                                # p-value=0.5891 > 0.05 do not rej
                        

# Levene’s Test for Homogeneity of variances
# Levene’s test is an equal variance test. It can be used to check if our data sets fulfill the homogeneity of variance assumption before we perform the t-test or Analysis of Variance

# H0: the compared groups have equal variance.
# H1: the compared groups do not have equal variance.

test_stat, pvalue = levene(test["Purchase"],
                           control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, value))           

                                # p-value=0.1083 > 0.05 do not reject
                                                                           
# Which statistical test did we use, and why?
# We used independent t-test because we want to determine if there is a significant difference between the means of two indepented groups, which may be related in certain features.

# What would be our recommendation to client?
# There is no statistically significant difference between the Control group that was served “maximum bidding” campaign and Test group that was served “average bidding” campaign. For this reason, we can recommend continuing with the maximum bidding campaign currently used.

# Conclusion
# Hypothesis established and interpreted
# The data was analyzed, outliers were observed
# It was checked whether the assumptions were met for the statistical test to be applied
# The assumptions were observed and tested
# Commented based on -p-value
# Suggestion offered to customer
