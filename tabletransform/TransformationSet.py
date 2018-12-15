from __future__ import division
import csv
import pandas as pd
import numpy as np
import itertools
import re


def transform_15(source_table, target_table):
    print(source_table)
    source_str = source_table.iloc[0, 0]
    target_str = target_table.iloc[0, 0]

    z = re.findall(r"[\w']+", source_str)
    x = re.findall(r"[\w']+", target_str)
    matches = 0

    try:

        if len(z) > len(x):
            a = len(z)
            b = len(x)
        else:
            b = len(z)
            a = len(x)

        for i in range(a):
            for j in range(b):
                if z[i] == x[j]:
                    matches += 1

        if matches == b:
            print("join")
            num = list(itertools.permutations(x, b))
        print(len(num))
        print(num)

        store = ''
        for m in num:
            if (list(m))== x:
                store = list(m)
                break

        print(store)
        order = []
    except:
        return "Not Valid"

    for i in store:
        p = 0
        for j in z:
            #print(j)
            if i == j:
                order.append(p)
            p = p + 1

    idx = order
    print('!!!')
    print(idx)

    #idx = New1.transform(source_str, target_str)
    ret = []
    for row in source_table.iloc[:, 0]:
        target_value = ''
        row_iter = re.findall(r"[\w']+", row)

        token_length = len(idx)
        source_to_target=''
        a=''
        if token_length > 5:

            for i in np.arange(token_length):
                source_to_target = source_to_target + row_iter[idx[i]]
                if i == 0:
                    source_to_target = source_to_target + ' '
                if i == 1:
                    source_to_target = source_to_target + ';('
                if i == 2:
                    source_to_target = source_to_target + ' '
                if i == 3:
                    source_to_target = source_to_target + ' '
                if i == 4:
                    source_to_target = source_to_target + '-'
                if i==5:
                    source_to_target = source_to_target + ' '
                if i==6:
                    source_to_target = source_to_target +' '
                if i == 7:
                    source_to_target = source_to_target + ')'
            print (source_to_target)
            ret.append(source_to_target)

        if token_length == 1:
            for i in np.arange(token_length):
                source_to_target = source_to_target + row_iter[idx[i]]
            print(source_to_target)
            ret.append(source_to_target)

        if token_length > 1 and token_length <= 3:
            for i in np.arange(token_length):
                source_to_target = source_to_target + row_iter[idx[i]]
                if i == 0:
                    source_to_target = source_to_target + ' '
            print(source_to_target)
            ret.append(source_to_target)

        if token_length == 4:
            for i in np.arange(token_length):
                source_to_target = source_to_target + row_iter[idx[i]]
                if i == 0:
                    source_to_target = source_to_target + ' '
                if i == 1:
                    source_to_target = source_to_target + ' ('
                if i==2:
                    source_to_target =source_to_target + '-'
                if i==3:
                    source_to_target = source_to_target +')'
            print(source_to_target)
            ret.append(source_to_target)

    return pd.DataFrame(ret)


def transform_14(X):

    #X = X.iloc[:, 0:1].values
    fixed = 'http://sina.sharif.edu/~'
    ret = []
    for index, row in X.iterrows():
        row = fixed + str(row[0])
        ret.append(row)
    return pd.DataFrame(ret)


def transform_13(X):

    #X = X.iloc[:, 0:1].values
    fixed = '*'
    ret = []
    for index, row in X.iterrows():
        row = str(row[0]) + fixed
        ret.append(row)
        #print(ret)
    return pd.DataFrame(ret)


# To Remove fixed and return First Middle Last
def transform_12(X):
    " This transformation removes Gov. from the front part of each string"
    fixed = 'Gov.'
    ret = []

    for index, row in X.iterrows():
        ret.append(row[0].replace(fixed, ''))

    return pd.DataFrame(ret)


# To Fixed First Middle Last
def transform_11(X):
    "This transformation adds Gov. to the front of each name string"
    #Y = transform_1(X)
    constant = 'Gov. '
    ret = []

    for index, row in X.iterrows():
        row = constant + str(row[0])
        ret.append(row)

    return pd.DataFrame(ret)


# To "First Initial. Last"
def transform_email1(X, domain, delimiter=''):
    # domain = '@gmail.com / sharif.edu / ymail.com'
    """This transformation adds domain at the last of each string"""

    transformed_df = pd.DataFrame(columns=['transformed'])
    emails = []

    sep = ''
    if 'sharif' in domain:
        sep = ' '

    for index, row in X.iterrows():
        names = row[0].split()
        print(names)
        if len(names) == 1:
            first = names[0].lower()
            emails.append(first + sep + domain)
        elif len(names) >= 2:
            first = names[1].lower()
            last = names[0].lower()
            emails.append(first[0] + delimiter + last + sep + domain)

    df = pd.DataFrame(emails)
    return df
    # abc = pd.Series(df.fillna('').values.tolist()).str.join('')
    # transformed_df = pd.Series.to_frame(abc)
    # return transformed_df


def transform_email2(X, domain, delimiter=''):
    # domain = '@gmail.com / sharif.edu / ymail.com'
    """This transformation adds domain at the last of each string"""

    transformed_df = pd.DataFrame(columns=['transformed'])
    emails = []

    sep = ''
    if 'sharif' in domain:
        sep = ' '

    for index, row in X.iterrows():
        names = row[0].split()
        print(names)
        if len(names) == 1:
            first = names[0].lower()
            emails.append(first + sep + domain)
        elif len(names) >= 2:
            first = names[0].lower()
            last = names[1].lower()
            emails.append(first + delimiter + last + sep + domain)

    df = pd.DataFrame(emails)
    return df
    # abc = pd.Series(df.fillna('').values.tolist()).str.join('')
    # transformed_df = pd.Series.to_frame(abc)
    # return transformed_df


def transform_email3(X, domain, delimiter=''):
    # domain = '@forsyth.k12.ga.us'
    """This transformation adds domain at the last of each string"""

    transformed_df = pd.DataFrame(columns=['transformed'])
    emails = []

    sep = ''
    if 'sharif' in domain:
        sep = ' '

    for index, row in X.iterrows():
        names = row[0].split()
        print(names)
        if len(names) == 1:
            first = names[0].lower()
            emails.append(first + sep + domain)
        elif len(names) >= 2:
            first = names[0].lower()
            last = names[1].lower()
            emails.append(first[0] + delimiter + last + sep + domain)

    df = pd.DataFrame(emails)
    return df
    # abc = pd.Series(df.fillna('').values.tolist()).str.join('')
    # transformed_df = pd.Series.to_frame(abc)
    # return transformed_df


def transform_5(X):
    '''This transformation returns first name, written in format Obama, Barack
    Obama, Barack => Barack
    '''

    newcsvdict = {"first name": []}
    for index, row in X.iterrows():
        names = row[0].split(',')
        if len(names) == 1:
            newcsvdict["first name"].append(names[0].strip())
        elif len(names) >= 2:
            fname_mname = names[-1]
            fname = fname_mname.strip().split()[0]
            newcsvdict["first name"].append(fname)

    df = pd.DataFrame.from_dict(newcsvdict)
    return df
    # abc = pd.Series(df.fillna('').values.tolist()).str.join('')
    # transformed_df = pd.Series.to_frame(abc)
    # return transformed_df


def transform_4(X):
    newcsvdict = {"first name": [], "middle name": [], "last name": []}
    for index, row in X.iterrows():
        names = row[0].split()

        last = " "
        middle = " "
        first = " "

        if len(names) == 1:
            first = names[0]
        elif len(names) == 2:
            first = names[1]
            last = names[0]
        elif len(names) >= 3:
            first = names[-1]
            middle = ' '.join(names[1:-1])
            last = names[0]

        newcsvdict["first name"].append(first[0] + '.')
        if middle.find('.') < 0 and len(middle) > 0:
            middle = ' ' + middle[0] + '. '
        newcsvdict['middle name'].append(middle)
        newcsvdict["last name"].append(last)

    df = pd.DataFrame.from_dict(newcsvdict)
    return df
    # abc = pd.Series(df.fillna('').values.tolist()).str.join('')
    # transformed_df = pd.Series.to_frame(abc)
    # return transformed_df
    # #return get_transformed_total(X, transformed_df)


# To Last, First Inital.
def transform_3(X):
    newcsvdict = {"last name": [], "first name": [], "middle name": []}
    try:

        for index, row in X.iterrows():
            names = row[0].split()
            last = " "
            middle = " "
            first = " "

            if len(names) == 1:
                first = names[0]
            elif len(names) == 2:
                first = names[1]
                last = names[0]
            elif len(names) >= 3:
                first = names[-1]
                middle = ' '.join(names[1:-1])
                last = names[0]

            newcsvdict["first name"].append(first)
            newcsvdict['middle name'].append(middle)
            newcsvdict["last name"].append(last + ', ')

        df = pd.DataFrame.from_dict(newcsvdict)
        abc = pd.Series(df.fillna('').values.tolist()).str.join('')
        transformed_df = pd.Series.to_frame(abc)
    except:
        return "Not Valid"
    return transformed_df
    #return get_transformed_total(X, transformed_df)


def transform_2(X):

    #Y = transform_1(X)
    ret = []
    # print("Y = ")
    # print(type(Y))
    # print(Y)
    for index, row in X.iterrows():
        row = '"' + str(row[0]) + '"'
        ret.append(row)

    return pd.DataFrame(ret)


def transform_1(X):
    newcsvdict = {"first name": [], "middle name": [], "last name": []}
    try:

        for index, row in X.iterrows():
            names = row[0].split()
            last = " "
            middle = " "
            first = " "

            if len(names) == 1:
                first = names[0]
            elif len(names) == 2:
                first = names[-1] + ' '
                middle = ''
                last = names[0]
            elif len(names) == 3:
                first = names[1] + ' '
                middle = names[-1] + ' '
                last = names[0]

            newcsvdict["first name"].append(first)
            newcsvdict['middle name'].append(middle)
            newcsvdict["last name"].append(last)

        df = pd.DataFrame.from_dict(newcsvdict)
        abc = pd.Series(df.fillna('').values.tolist()).str.join('')
        transformed_df = pd.Series.to_frame(abc)
    except:
        return "Not Valid"
    return transformed_df
    #return get_transformed_total(X, transformed_df)


def get_transformed_total(X, transformed_df):
    return pd.concat([transformed_df, X.drop(X.columns[0], axis=1)])