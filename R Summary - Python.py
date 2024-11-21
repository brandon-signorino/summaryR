# for testing
import numpy as np
import pandas as pd

# dependencies:
#   pandas (since designed to work with Pandas dataframes)
#   pandas.api.types.is_float_dtype (to test for float dtypes)
#   pandas.api.types.is_integer_dtype (to test for integer dtypes)
#   pandas.api.types.is_datetime64_any_dtype  (to test for datetimes)
# arguments:
#   df = Pandas DataFrame
#   int_as_float = boolean; if True, treat integers as numerical (so will give numerical stats instead of value counts)
#   value_count_threshold = integer
#       - if >1, will group value counts below threshold and sum them,
#       - as long as more than one value count falls below threshold;
#       - otherwise, will display all individual value counts 
#       - (shortens some long outputs, e.g. 100 categories would be way too long)
#   prettyPrint = boolean; if True, pretty-print to console (similar to R summary() output)
# returns:
#   summary_dict = dictionary with column names and relevant info 
#       - keys = column names from df
#       - values = pd.Series with relevant summary info, index = name of each feature
# notes:
#   - make sure column dtypes are set how you want before calling this function
#   - will treat any non-numerical columns as 'object' dtype for simplicity
#   - for dates: 
#       - if being used as dates, make sure they are datetime64
#       - if being used as categories/groups, make sure they are strings/objects

def summaryR(df, int_as_float = False, value_count_threshold = 1, prettyPrint = False):

    # import dependencies
    # import pandas as pd  # can only be used on pd.DataFrame, so should assume already imported?
    from pandas.api.types import is_integer_dtype, is_float_dtype, is_datetime64_any_dtype  # for testing for different dtypes
    
    # make sure only pd.DataFrame is passed to df argument
    if not isinstance(df, pd.DataFrame):  
        raise TypeError(f"Pandas DataFrame expected, got '{type(df).__name__}'")

    # make sure only boolean value is passed to int_as_float argument
    if not isinstance(int_as_float, bool):  
        raise TypeError(f"boolean value expected, got '{type(int_as_float).__name__}'")

    # make sure only integer is passed to value_count_threshold
    if not isinstance(value_count_threshold, int):  
        raise TypeError(f"integer expected, got '{type(value_count_threshold).__name__}'")

    # make sure only boolean value is passed to prettyPrint argument
    if not isinstance(prettyPrint, bool):  
        raise TypeError(f"boolean value expected, got '{type(prettyPrint).__name__}'")

    # initialize dict of column -> info
    summary_dict = {}  

    # iterate through columns of df, adding info for each to dict
    for column in df:  
        
        # floats...
        if is_float_dtype(df[column]):  
            summary_dict[column] = df[column].describe(include = 'all') # numerical stats
            if df[column].isna().sum() > 0:
                summary_dict[column]['nulls'] = df[column].isna().sum()  # count null values
            summary_dict[column]['dtype'] = df[column].dtype  # get column dtype

        # integers being treated as floats...
        elif int_as_float and is_integer_dtype(df[column]):  
            summary_dict[column] = df[column].describe(include = 'all')  # numerical stats
            if df[column].isna().sum() > 0:
                summary_dict[column]['nulls'] = df[column].isna().sum()  # count null values
            summary_dict[column]['dtype'] = df[column].dtype  # get column dtype

        # datetime...
        elif is_datetime64_any_dtype(df[column]):  
            # summary_dict[column] = df[column].describe(include = 'all')  # may need to remove datetime_is_numeric, depending on platform
            summary_dict[column] = df[column].describe(include = 'all', datetime_is_numeric = True)  
            if df[column].isna().sum() > 0:
                summary_dict[column]['nulls'] = df[column].isna().sum()  # count null values
            summary_dict[column]['dtype'] = df[column].dtype  # get column dtype
        
        # treat all other dtypes as objects
        else:  
            valueCounts = df[column].astype('object').value_counts(dropna = False)  # value counts, including nulls
            if (value_count_threshold > 1) and (len(valueCounts[valueCounts < value_count_threshold]) > 1):  # only roll up "other_count" if more than 1 group fell under the threshold
                summary_dict[column] = valueCounts[valueCounts >= value_count_threshold]  # only counts >= threshold
                summary_dict[column]['other_count *'] = valueCounts[valueCounts < value_count_threshold].sum()  # sum together all others
                summary_dict[column]['dtype'] = df[column].dtype  # get column dtype
                summary_dict[column]['* note:'] = "at least two value counts <" + str(value_count_threshold) + " threshold"  # note
            else:  # if only one or no other groups fell under threshold
                summary_dict[column] = valueCounts  # provide all value counts
                summary_dict[column]['dtype'] = df[column].dtype  # get column dtype                

    if prettyPrint:
        print("\n\n".join("\033[1m{}:\n\033[0m{}".format(k, v.to_string()) for k, v in summary_dict.items()))  
            # "\033[1m" bolds column name text; "\033[0m" resets to normal text
            # to_string removes name and dtype from end of output of each series, just for more tidy printing

    # return completed dict, so all parts can be accessed later
    return summary_dict


# extract modified version of iris dataset... 
# 5 null rows added
# added col of int version of class
# added col of dummy date sequence
iris_df_mod = pd.read_pickle("iris_df_mod.pkl")

# summaryR(iris_df_mod, int_as_float = True, prettyPrint = False)
# summary_dict = summaryR(iris_df_mod, int_as_float = False, prettyPrint = False)

# summaryR(iris_df_mod, int_as_float = False, prettyPrint = True)

# summary_dict = summaryR(iris_df_mod, int_as_float = True, prettyPrint = True)

summary_dict = summaryR(iris_df_mod, int_as_float = False, value_count_threshold = 6, prettyPrint = True)


# examples of usage... 

# summary_dict
# summary_dict['Sepal_Length']
# summary_dict['Sepal_Length']['nulls']
# summary_dict['Class']
# summary_dict['Class'][None]
# summary_dict['class_int']
# summary_dict['class_int'][pd.NA]

# example of handling an argument error
# summaryR(iris_df_mod, prettyPrint = 5)