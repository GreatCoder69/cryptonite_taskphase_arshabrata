# Pandas for Machine Learning
## Introduction
Pandas is a powerful and widely used data manipulation and analysis library in Python. It is built on top of NumPy and provides flexible data structures, particularly DataFrames and Series, which are well-suited for working with labeled data. With Pandas, we can quickly perform common tasks in data analysis, enabling efficient exploration and manipulation of large datasets, making it an essential tool in data science and machine learning.
## Downloading and importing pandas
```
pip install pandas
pip install numpy
```
We must first install the pandas and numpy libraries.
```
import pandas as pd
import numpy as np
```
This imports the necessary packages for pandas and numpy.
### Pandas series
Pandas series is a 1-dimensional array holding any type of data.
```
s=[1,2,3,4,5]
var=pd.Series(s)
```
This will print the data members in the array along with their indices in a two-column table format.
```
var[3]
```
This wil print the element at index 3, which is 4 in this case.
```
s=[1,2,3,4,5]
var=pd.Series(s)
s_ind=["a","b","c","d","e"]
var1=pd.Series(s,s_ind)
```
Here we also specify the index values for our series. Therefore, instead of the indices starting from 0, we get the elements of s_ind passed as the second argument in the index column while printing var1.
```
var1["c"]
```
Here, instead of using the typical index values, we use the new index values we just assigned.  
This prints the element at index "c" which is 3 in this case. Keep in mind, we can also use the index number even when separate indices are assigned.
```
test={"apple":5,"banana":9,"mango":12}
var2=pd.Series(test)
```
Here we turn a key value dictionary to a pandas series.  
The resultant of var2 is that the string becomes the index of the series while the number here becomes the value at that index.  
So on printing we get apple in index column and 5 in element column and so on.

### Data Frames
```
from numpy.random import randn
data=randn(4,3)
```
Here first and second arguments are number of rows and columns respectively.  
We build a mXn matrix of random numbers. 
```
rows=["A","B","C","D"]
cols=["Monday","Tuesday","Wednesday"]
```
We set the row and column headers for our dataframe.
```
mydf=(data,rows,cols)
```
This creates our required dataframe. PHOTO LAGA.    
```
import csv file
mydf1=pd.read_csv('housingdata.csv')
```
This reads a csv file which means a comma separated values file and turns it into a dataframe.  
Since I am considering the csv file to be in the same directory, I am using a relative path.
```
mydf.loc[1]
```
This pulls out the row at index 1.
```
mydf.loc[[0,5]]
```
This pulls out the rows at indices contained in the list inside the argument section, which is 0 and 5 in this case.
```
mydf.head()
```
This pulls the first 5 rows.
```
mydf.head(9)
```
This pulls the first 9 rows
```
mydf.tail()
```
This pulls the last 5 rows.
```
mydf.tail(7)
```
This pulls the last 7 rows.
```
mydf.info()
```
Gives information about the dataframe like names and no. of rows and columns, no. of entries, no. of non-null entries and so on.
```
mydf.shape
```
Gives the shape of the dataframe.
```
mydif.ndim
```
Gives the number of dimensions.
```
mydf.dtypes
```
Gives the datatype of the columns.
```
mydf.describe()
```
Gives the statistics of the data of a column like mean,standard deviation, minimum and so on.
```
mydf["Name_of_column"].describe()
```
Gives statistics of the particicular column.
```
mydf["column_name"]
mydf.column_name
```
These return the column in a pandas series format.
```
mydf.iloc[:,0]
```
Here the ":" signifies we want the whole column and the 0 is the column number. Returns in pandas series format.
```
mydf["column_name"].value_counts()
```
Gives the distinct values in the column in descending order.
```
mydf["column_name"].value_counts(ascending=True)
```
We set the ascending order flag to true and this gives the distinct values in the column in ascending order. 
```
mydf["column_name"].value_counts(dropna=False)
```
By default if any value is NaN, it is not displayed. We can change that by setting dropna flag to false.
```
mydf["column_name"].value_counts(normalize=True)
```
This gives us the frequency (relative frequency) of distinct elements. To obtain percentage we must multiply by 100.
```
mydf["column_name"].value_counts()["item_name"]
```
This gives us the count of a specific item in the column.
```
mydf.groupby("column_name").size()
```
Groups the unique values by size.
```
mydf.groupby("column_name").count()
```
Groups the unique values by count.
```
mydf.apply(pd.value_counts)
```
This gives us a count of all columns across all columns. Generally lot of NaN encountered as column data is generally unique.
```
gender=["male","female","female","male","male"]
mydf["Gender"]=gender
```
This adds a new column to our dataframe along with the values inside the list being entered in the rows.  
Note that list size and no. of rows should match.
```
mydf["Alive/Dead"]=["Alive"]*len(mydf)
```
This sets a default value to all the rows in our new column to prevent any errors.
```
mydf["new_column"]=[np.nan]*len(mydf)
```
We set all values in the new column to NaN.
```
mydf.insert(2,"new_column",[True]*len(mydf),True)
```
First argument is position of column.  
Second argument is name of column.  
Third argument is value inside rows.  
Fourth argument is boolean to allow or disallow duplicates.
```
mydf2=mydf.assign(new_column=["Hello"]*len(mydf))
```
Creates a new dataframe by adding a new column at end with the entered value in rows.
```
mydf.drop("col_name",axis=1)
```
We delete the column and we must specify the axis to be 1 since axis of the row headers is 0 and without specifying, the default in drop function is axis 0.
```
mydf.drop(3)
```
This deletes the row at index 3.  
Remember that the drop function only works when invoked, if dataframe is printed again then the deleted row shows up again.
```
mydf.loc[2]
```
Pulls the location of the row at specified index and it can take string if indices are strings.
```
mydf.iloc[2]
```
Pulls the location of the row at specified integer index.
```
mydf.loc[2,3]
```
Pulls the data at the specified row and column number
```
mydf.loc[['row','row'],['col','col']]
mydf.loc[[1,3],["name","breed"]]
```
This gives the data of name and breed at the row numbers 1 and 3.
```
mydf=="BROWN"
```
Returns the whole dataframe filled with boolean and displaying true wherever brown is written.
```
mydf>159
```
Same specifications but different conditional operator.
```
mydf[mydf=="BROWN"]
```
Returns the dataframe where false is NaN and BROWN is written wherever it is found in the dataframe.
```
mydf[mydf=="BROWN"]["col_name"]
```
Returns only the column with the specifications of the syntax aboved.
```
mydf[mydf=="BROWN"]["col1","col2"]
```
Same specifications but the rows displayed are increased.
```
mydf[(mydf["Color"]=="BROWN") & (mydf["Breed"]=="Mixed")]
```
Multiple conditionals joined using and.
```
mydf[(mydf["Color"]=="BROWN") | (mydf["Breed"]=="Mixed")]
```
Multiple conditionals joined using or.
```
mydf[(mydf["Color"]=="BROWN") & (mydf["Breed"]=="Mixed")]["col_name"]
```
Restricts output to only specified column.
```
mydf["Frame Header"]=["col1","col2","col3","col4","col5"]
mydf.set_index("Frame Header",inpace=True)
```
This sets the added column to be the index column of the dataframe. We must set inplace to true to make the change permanent.
```
mydf.reset_index(inplace=true)
```
We reset our index column.
```
mydf.dropna()
```
It drops all rows which contains NaN.
```
mydf.dropna(axis=1)
```
It drops all columns which contains NaN.  
Note: Row headers are at axis 0 and column headers are at axis 1.
```
mydf.dropna(thresh=2,axis=1,inplace=true)
```
Sets threshold to 0. Deletes columns where there are 2 NaN.
```
mydf.fillna(value=69)
```
Replaces all NaN with the specified value.
```
mydf.fillna(value=mydf["col_name"].mean())
mydf.fillna(value=mydf["col_name"].min())
```
We can use math functions to replace the NaN values.
```
company=mydf.groupby("Corporation")
```
The location of object where all companies are grouped is stored in the variale company.  
We can perform all math functions on this and printing prints the result of the math function on each grouped dataset.
```
company.sum()
company.max()
company.min()
company.mean()
company.var()
company.std()
company.count()
company.describe()
```
Performing math functions.
```
mydf["Name"].value_counts()
```
Returns a count of all unique entries in the column.
```
pd.DataFrame(mydf["Name"].value_counts().head())
```
Converts to a dataframe.
```
mydf["Name"].unique()
```
Returns all entries which are there only once.
```
pd.DataFrame(mydf["Name"].unique())
```
Converts to Data Frame.
```
def times1000(x):
    return x*1000
```
Write a function which we want to apply.
```
mydf["Salary"].apply(times1000)
```
Multiplies all entries in salary column by 1000.
```
mydf["Salary"].apply(lambda x:x*1000)
```
Using lambda function to achieve the same output.
```
mydf["Salary"]=mydf["Salary"].apply(lambda x:x*1000)
```
Updates the column in original dataframe.
```
def appender(x):
    return "hello "+x
```
Write a function to use in the next step.
```
mydf[["Name","Company"]].apply(appender)
```
Applies the function to both the columns.
```
mydf.sort_values("Col_name")
```
Sorting the dataframe according to ascending order of values in the column.
```
mydf.sort_values("Col_name",ascending=False,inplace=true)
```
Sorting the dataframe according to descending order of values in the column.
```
mydf.sort_values("Names")
```
Sorts the names in alphabetical order.
```
mydf.sort_values("Names",ascending=False)
```
Sorts the names in reverse alphabetical order.