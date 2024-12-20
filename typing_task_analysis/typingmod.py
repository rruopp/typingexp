import numpy as np
import pandas as pd
import ast
import math
import matplotlib.pyplot as plt
from scipy.stats import variation

#### STRING AND BIGRAM LIST GROUPINGS ####

## list of all strings
all_strings = ['there', 'think', 'about', 'would', 'lucky', 'buddy',
          'cheer', 'theme', 'belly', 'champ', 'puppy', 'vodka',
          'tithe', 'therm', 'haole', 'cooed', 'faqir', 'druze',
          'edthe', 'heond', 'kremp', 'vanru', 'zibja', 'pykka']

## string groupings by word frequency (WF)
highwf = ['there', 'think', 'about', 'would', 'lucky', 'buddy']
medwf = [ 'cheer', 'theme', 'belly', 'champ', 'puppy', 'vodka']
lowwf = ['tithe', 'therm', 'haole', 'cooed', 'faqir', 'druze']
pseudo = ['edthe', 'heond', 'kremp', 'vanru', 'zibja', 'pykka']

## string groupings by bigram frequency (BF)
avg_highbf = ['there', 'think',  'cheer', 'theme', 'tithe', 'therm', 'edthe', 'heond']
avg_medbf = ['about', 'would', 'belly', 'champ', 'haole', 'cooed', 'kremp', 'vanru']
avg_lowbf = ['lucky', 'buddy', 'puppy', 'vodka', 'faqir', 'druze', 'zibja', 'pykka']

# dataframe of bigram frequencies in descending order
bg_freqs = pd.read_csv('bg_freqs.csv').drop(labels=['Unnamed: 0'], axis=1)
bg_freqs = bg_freqs.sort_values(by='Frequency', ascending=False, ignore_index=True)

# list of all bigrams in order of descending bigram frequency
all_bigrams = bg_freqs['Bigrams']

# bigrams by bigram frequency groupings in descending order
highbf = list(bg_freqs['Bigrams'].loc[0:15])
medbf = list(bg_freqs['Bigrams'].loc[16:46])
lowbf = list(bg_freqs['Bigrams'].loc[47:72])

## lists of string groupings
wf_types = [highwf, medwf, lowwf, pseudo]
avgbf_types = [avg_highbf, avg_medbf, avg_lowbf]

## list of bigram groupings
bf_types = [highbf, medbf, lowbf]

## lists of bigrams with and without bigrams of repeated letters
medbf_reps = ['ll', 'ee', 'oo', 'pp']    
medbf_norep = list(filter(lambda x: x not in medbf_reps, medbf))

lowbf_reps = ['dd', 'kk']
lowbf_norep = list(filter(lambda x: x not in lowbf_reps, lowbf))

### BIGRAM FUNCTIONS ###

## defining function that separates words in to bigrams
def bi_byword(word):
    bi_results = []
    for y in range(0, (len(word)-1)):
        bigram = word[y] + word[y+1]
        bi_results.append(bigram)
    return bi_results

#### DATAFRAME FILTERING FUNCTIONS ####

## defining function to make dataframe of only correct trials
def correct_filter(DF):
    corr_temp = []
    for index, data in DF.iterrows():
        if data['string'] == data['resp_string']: ## compares presented string with typed response
            corr_temp.append(DF.iloc[index])
    corr = pd.DataFrame(corr_temp).reset_index(drop=True)
    return corr

## defining function to make dataframe of only incorrect trials
def incorrect_filter(DF):
    incorr_temp = []
    for index, data in DF.iterrows():
        if data['string'] != data['resp_string']: ## compares presented string with typed response
            incorr_temp.append(DF.iloc[index])
    incorr = pd.DataFrame(incorr_temp).reset_index(drop=True)
    return incorr

## defining function to filter for only trial rts
def rt_columns(DF):
    rt_columns = ['sID', 'trial_num', 'string']
    for column in DF:
        if 'key_resp.rt' in column:
            rt_columns.append(column)
        else:
            pass
    rts = DF[rt_columns]
    return rts

#### IKI FUNCTIONS ####

### For all these functions, the dataframe variable (DF) needs to be a reaction time DF with associated strings in column 1 (ex. all_rts, corr_rts, incorr_rts)
## defining function to determine interkey intervals for each trial
def iki(DF):
    ints_byword = []
    last_key = len(DF.columns) - 1  
    print(last_key)
    for index, data in DF.iterrows():
        intervals = []
        for n in range(4, last_key):
            interval = (DF.iloc[index, n]) - (DF.iloc[index, n - 1])
            intervals.append(interval)
        ints_byword.append(intervals)
    all_ints = pd.DataFrame(ints_byword)
    all_ints[all_ints < 0] = 0  ## making all negative values in initial output 0
    all_ints.insert(0, 'string', DF['string'], True) ## adding in column containing the string typed each trial
    return all_ints

## defining function to determine coefficient of variation (CV) across interkey intervals (IKIs) for trials with the same word
def cv_byword(string, DF):
    arr = iki(DF)
    sort_byword = []
    for index, data in arr.iterrows():
        if DF['string'][index] == string:
            sort_byword.append(data)
    iki_byword = pd.DataFrame(sort_byword)
    temp = iki_byword.drop(['string'], axis=1) ## temporatily dropping 'string' column to calculate CV across columns
    iki_cv = (variation(temp, axis=0)).tolist()
    iki_cv.insert(0, string)
    return iki_cv
    
## defining function to make dataframe of all IKI-CVs by word
def cv_all(str_type, DF):
    cvs = []
    for x in str_type:
        y = cv_byword(x, DF)
        cvs.append(y)
    all_cvs = (pd.DataFrame(cvs)).dropna(axis=1) ## dropping columns with NaNs -- IKI-CVs of additive errors, not necessary to analyze
    return all_cvs

## defining function to determine average IKI-CV by word freq. type
def avg_cv(str_type, DF):
    arr = cv_all(str_type, DF)
    avgs = []
    last_row = len(arr.columns)
    for n in range(1, last_row):
        y = arr[n].mean()
        avgs.append(y)
    return avgs

## defining function to determing CV IKI of each bigram
def cv_bybg(bigram, DF):
    bi_ikis = []
    for index, row in DF.iterrows():
        old_bi = DF['Bigram'][index]
        new_bi = ((old_bi).replace("'", "")).replace(" ", "")
        if new_bi == bigram:
            bi_ikis.append(DF['IKI'][index])
    bi_cviki = (variation(bi_ikis, axis=0)).tolist()
    return bi_cviki

## defining function to determine CV IKI for all bigrams
def cv_allbgs(DF):
    cvs = []
    for bigram in all_bigrams:
        cv = cv_bybg(bigram, DF)
        cvs.append([bigram, cv])
    return cvs

#### ONSET DELAY FUNCTIONS ####

## defining function for calculating onset delays for different WF categories
def onset_delay(DF):
    return DF['key_resp.rt.1']

## defining function for calculating average onset delay for different WF categories
def avg_onset_delay(DF):
    return np.mean(DF['key_resp.rt.1'])

#### TYPING TIME FUNCTIONS ####

## defining function to determine time spent typing each trial (effectively speed)
def time_typing(DF):
    speeds = []
    key_1 = len(DF.columns)
    for index, data in DF.iterrows():
        for n in range(-1, -(key_1), -1):
            if DF.iloc[index, n] != 0: ## finds last rt value that isn't zero, so typing time is not a negative number
                speed = (DF.iloc[index, n]) - (DF.iloc[index, 1])
                speeds.append(speed)
                break
    return speeds

#### DELTA IKI FUNCTIONS ####

## defining function to determine delta IKIs by word
def diki(string, DF):
    all_ikis = iki(DF)
    sort_byword = []
    for index, data in all_ikis.iterrows():
            if all_ikis['string'][index] == string:
                sort_byword.append(data)
    iki_byword = pd.DataFrame(sort_byword)
    iki_byword.reset_index(drop=True, inplace=True)
    last_key = len(iki_byword.columns)
    trial_count = len(iki_byword)
    dikis_byword = []
    for index in range(0, trial_count - 1):
        dikis = []
        for n in range(1, last_key):
            diki = abs((iki_byword.iloc[index + 1, n]) - (iki_byword.iloc[index, n])) # solves for delta IKI and makes value absolute
            dikis.append(diki)
        dikis_byword.append(dikis)
    dikis_byword = pd.DataFrame(dikis_byword)
# make a list of row titles (inter-repetition position)
    row_titles = []
    for n in range(1, trial_count):
        y = '%s-%s' %(n, n+1)
        row_titles.append(y)
    dikis_byword.insert(0, 'inter-rep', row_titles)
    return dikis_byword

## defining function to determine average of all delta IKIs within word
def avg_diki_byword(string, DF):
    dikis_byword = diki(string, DF)
    avgs = []
    last_row = len(dikis_byword.columns)
    dikis_byword['mean'] = dikis_byword.mean(axis=1, numeric_only=True)
    meandiki_bypos = dikis_byword['mean']
    return meandiki_bypos

## defining function to determine the average delta IKI by word type -- average of average delta IKI per word
def avg_diki_byWF(str_type, DF):
    allword_dikis = pd.DataFrame()
    for string in str_type:
            dikis_byword = diki(string, DF)
            dikis_byword_df = pd.DataFrame(dikis_byword)
#             print(dikis_byword_df)
            allword_dikis = allword_dikis.append(dikis_byword_df)
    allword_dikis = allword_dikis.reset_index(drop=True)
# get average of word-specific delta IKI averages for each inter-repetition position
    avgiki_bypos = []
    for n in range(1, 10):
        iki_bypos = pd.DataFrame()
        for index, data in allword_dikis.iterrows():
            if allword_dikis['inter-rep'][index] == '%s-%s' %(n, n+1):
                temp = allword_dikis.iloc[index]
#                 print(temp)
                iki_bypos = iki_bypos.append(temp)
        iki_bypos['mean'] = iki_bypos.mean(axis=1)
#         print(iki_bypos)
        double_mean = iki_bypos['mean'].mean(numeric_only=True)
        avgiki_bypos.append(double_mean)
    return avgiki_bypos