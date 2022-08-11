#checking if it is equals
 data_df['Sentiment'].value_counts()

 #number of positive
 max_class = len(data_df[data_df['Sentiment']==0]) 
 #number of negative 
 min_class = len(data_df[data_df['Sentiment']==1]) 


 positiveRet = data_df[data_df['Sentiment']==0].sample(n = max_class)
 negativeRet = data_df[data_df['Sentiment']==1].sample(n = min_class)
 #creating the dataframe
 balancedData = positiveRet.append(negativeRet)
 # to keep track the remaining number of reviews
 remain = max_class 
 remain = remain - min_class

 #duplicate the negative or the 1
 while remain > 0:
   if remain <=  min_class:
     negativeRet = data_df[data_df['Sentiment']==1].sample(n = remain)
   else:
     negativeRet = data_df[data_df['Sentiment']==1].sample(n = min_class)
   remain = remain - min_class
   balancedData = balancedData.append(negativeRet)


 # .sample() mix up he rows, sets frac=1 to take all the rows,
 #.reset_index() with drop=True option to remove the real indexes and restart new indexing.
 balancedData = balancedData.sample(frac=1).reset_index(drop=True)


 #checking if it is equals now
 balancedData['Sentiment'].value_counts()
