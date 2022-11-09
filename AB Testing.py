##################################################################
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

#####  Görev 1: Veriyi Hazırlama ve Analiz Etme
## Adım 1: ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test grubu verilerini ayrı değişkenlere atayınız

control = pd.read_excel("ab_testing.xlsx", sheet_name="Control Group")
test = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")

## Adım 2: Kontrol ve test grubu verilerini analiz ediniz.

control.describe().T
test.describe().T

## Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.

df = pd.concat([control, test], axis=0, ignore_index=True )
df.head()

