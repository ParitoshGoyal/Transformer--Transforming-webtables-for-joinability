from __future__ import division
import os
import pandas as pd
import fuzzyset
import TransformationSet
import numpy as np
import sys
import re
import itertools

source_path = r'dataset\source\source15.csv' #change the path based on what table one wants to test
target_path = r'dataset\target\target15.csv' #

source_file = pd.read_csv(source_path, delimiter=',')
target_file = pd.read_csv(target_path, delimiter=',')

print(source_file.shape)
rows, _ = source_file.shape
print(rows)
print(_)


def fuzzmatch (source_file, target_file):

    source_key = [column for column in source_file][0]
    target_key = [column for column in target_file][0]
    source_new_df = pd.DataFrame(columns=[column for column in source_file])
    target_new_df = pd.DataFrame(columns=[column for column in target_file])
    # mapping={}
    fuzzy_threshold = 0.125

    for i, row_source in source_file.iterrows():
        fuzzymatch = fuzzyset.FuzzySet()
        fuzzymatch.add(row_source[source_key])
        for j, row_target in target_file.iterrows():
            fuzzyval = fuzzymatch.get(row_target[target_key])
            #print(row_source[col1]) row_target[col1]
            if fuzzyval is None:
                continue
            elif fuzzyval[0][0] > fuzzy_threshold:
#                print(fuzzyval)
                #add these rows to new dataframes
                source_new_df = source_new_df.append(row_source)
                target_new_df = target_new_df.append(row_target)
        del fuzzymatch
    return source_new_df, target_new_df


def transformed_mean_score(transformed_set, target_set):
    score = 0
    for index, row in transformed_set.iterrows():
        fs = fuzzyset.FuzzySet()
        fs.add(row[0])
        fuzzyval = fs.get(target_set.iloc[index, 0])
        if fuzzyval is None:
            continue
        curr_score = fuzzyval[0][0]
        #curr_score = fs.get(target_set.iloc[index, 0])[0][0]
        # print("curr_score = ")
        # print(curr_score)
        score += curr_score
        del fs
    return score/transformed_set.shape[0]

def best_transformation(transformed_sets, target_set):

    highest_mean = 0; highest_mean_index = 0
    for i in range(len(transformed_sets)):
        if type(transformed_sets[i]) != type("Not Valid"):
            score = transformed_mean_score(transformed_sets[i], target_set)
            if score > highest_mean:
                highest_mean = score
                highest_mean_index = i

    return highest_mean_index, transformed_sets[highest_mean_index]


X, Y = fuzzmatch(source_file, target_file)

Z = None


Tf15 = TransformationSet.transform_15(X, Y)
#Tf15.to_csv('target24abctf15.csv')
Tf14 = TransformationSet.transform_14(X)
Tf13 = TransformationSet.transform_13(X)
Tf12 = TransformationSet.transform_12(X)
Tf11 = TransformationSet.transform_11(X)
Tf10 = TransformationSet.transform_email1(X, "sharif.edu", '')
Tf9 = TransformationSet.transform_email2(X, "@gmail.com", '')
Tf8 = TransformationSet.transform_email2(X, "@hotmail.com", '')
Tf7 = TransformationSet.transform_email2(X, "@ymail.com", '')
Tf6 = TransformationSet.transform_email3(X, '@forsyth.k12.ga.us', '')
Tf5 = TransformationSet.transform_5(X)
Tf4 = TransformationSet.transform_4(X)
Tf3 = TransformationSet.transform_3(X)
Tf2 = TransformationSet.transform_2(X)
Tf1 = TransformationSet.transform_1(X)

Tf_set = [Tf1, Tf2, Tf3, Tf4, Tf6, Tf7, Tf8, Tf9, Tf10, Tf11, Tf12, Tf13, Tf14, Tf15]

best_transform_index, best_transformed_set = best_transformation(Tf_set, Y)
best_transform_index = best_transform_index +1 #contains the id of best possible transformation for given table.

#Example: if Tf15 comes out to be the best transformation for a given input table, best_transform_index will contain 15, this will be printed at the end of the program as well.



TX = X
TY = Y
#
# TX['transform'] = Tf15

TX = TX.reset_index(drop=True)
TY = TY.reset_index(drop=True) # we use TX, TY for performing final join operations, this was done individually for each given input pair of tables.

print('index = ')
print(best_transform_index)
