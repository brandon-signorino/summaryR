# `summaryR()`
**creating a Python equivalent to R's summary() function, to use with Pandas DataFrames**

The impetus for this project is quite simple.  In grad school, my first two courses consisted of learning R and Python at the same time.  Ever since that term, I have noticed a gap between the two when it comes to exploratory data analysis.  When beginning a data analysis project in R, the first thing I do after loading a dataset is to call the `summary()` function.  
<img src="https://github.com/user-attachments/assets/3a7d158f-ba00-4006-a44b-caed7710bf6c" alt="drawing" width="600"/>

This function displays numerical statistics (minimum, mean, quantiles, etc.) for numerical columns, counts of unique values for text columns, counts of null values, and so on... all in one single function.  There simply is not a single function in Python that does the same thing in one go; questions [like this one on Stack Overflow](https://stackoverflow.com/questions/33889310/r-summary-equivalent-in-numpy) demonstrate the need for something like the convenient function in R, and I always find myself wanting to use that R function whenever I build a new Pandas DataFrame.

So, I decided to make a Python version myself: a single function that, when called, gives similar summary info and can display it nicely to the console.  For this project, I have tried to stick to the following principles and scope:
- Limit usage to Pandas DataFrames
- Keep it simple and lightweight... don't overcomplicate it
- Strive for console output that is close to what `summary()` gives in R
- Make it helpful by returning something useful to access the information generated

As of the creation of this repository, the console output is pretty close to what I hoped for:
<img src="https://github.com/user-attachments/assets/0fb22695-b82c-4258-ae1a-6e96d0b7bbbc" alt="drawing" width="700"/>

The only visual thing I am still trying to figure out is if there is a way to display those items in a sort of grid (each column's info in its own "cell", similar to how R does it), so that scrolling does not have to be so long for large datasets.  However, I am sure I am missing traps for some potential problems and other potential improvements.  I don't necessarily want to expand its functionality very much (aside from doing more of what the R `summary()` function can do, perhaps with different data types), but I definitely want to make it more robust within the existing scope.  That is why I decided to create a GitHub account and create this repository.
