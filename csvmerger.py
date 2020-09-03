
import pandas as pd

ad_coln=['category','content' , 'contentURL'] #3 columns
sz_coln=['category','content' ] #2 columns
ad = (pd.read_csv('ad.csv', names=ad_coln, header=None)).dropna()
sz = (pd.read_csv('sz.csv', names=sz_coln, header=None)).dropna()

sz = sz.drop(index=0)
# in some scenarios, when you download your csv file, the 0th Row of your index will be the headers of each of your columns
#since that was the isse when i downloaded sz.csv we will drop said row and the new list of values from sz_column will precede and be the headers of each column.
sz = sz.reset_index(drop=True)

frames = [ad,sz]
adsz = pd.concat(frames)
adsz = adsz.reset_index(drop=True)
#since the 2 csv files have different number columns and we are merging them I chose to replace all the 
#cells with no data(they were assigned values of '.') with empty strings("").

adsz = adsz.fillna(".")
adsz = adsz.replace("." , "")
dataset = adsz.to_csv('dataset.csv')
