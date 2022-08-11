# BalancedDataFrame
balancing dataframe by duplication of one label python


To achieve that balanced dataframe we took the number of positive reviews as “max_class”, and the number of negative reviews as “min_class”, then we append the negative reviews to the end of the positive reviews and save it as a new dataframe called “balancedData” by using pandas’ .append() function.

Next, we initialize a variable called “remain” that used to keep track the remaining number of reviews,  to use it in the while loop that iterates if there is any remain ( the number of the negative reviews on “balancedData” is still less than the positive) and check if it's bigger than the min_class it will take all of the negative reviews and duplicate them, then append it again to balancedData. 

However, if the remain “let's say it’s equal to K” is less than min_class, it will take a random sample of size K by attaching K as a parameter for .sample() function, and then append it again to balancedData and then the loop will end because the remain is less than 1. 
