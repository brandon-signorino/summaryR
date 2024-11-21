# summaryR
**creating a Python equivalent to R's summary() function, to use with Pandas DataFrames**

The impetus for this project is quite simple.  In grad school, my first two courses consisted of learning R and Python at the same time.  Ever since that term, I have noticed a gap between the two when it comes to exploratory data analysis.  When beginning a data analysis project in R, the first thing I do after loading a dataset is to call the `summary()` function.  This allows me to see numerical statistics (minimum, mean, quantiles, etc.) for numerical columns, counts of unique values for text columns, and so on... all in one single function.  There simply is not a single function in Python that does the same thing in one go; questions [like this one on Stack Overflow](https://stackoverflow.com/questions/33889310/r-summary-equivalent-in-numpy) demonstrate the need for something like the convenient function in R, and I always find myself wanting to use that R function whenever I build a new Pandas DataFrame.

So, I decided to make one myself.  I try to stick to the following principles and scope:
- Limit usage to Pandas DataFrames
- Keep it simple and lightweight... don't overcomplicate it
- Strive for console output that is close to what `summary()` gives in R
- Make it helpful by returning something useful to access the information generated

As of creation of this repository... (to be continued)
