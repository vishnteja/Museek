import pandas as pd

f_path = 'data/songdata.csv'
data_orig = pd.read_csv(f_path)
data = pd.read_csv(f_path)

#print(data.dtypes)
data['text']=data['text'].apply(lambda x:str(x).replace('.',''))
data['text']=data['text'].apply(lambda x:str(x).replace(',',''))
data['text']=data['text'].apply(lambda x:str(x).replace('?',''))
data['text']=data['text'].apply(lambda x:str(x).replace('!',''))
data['text']=data['text'].apply(lambda x:str(x).replace('"',''))
data['text']=data['text'].apply(lambda x:str(x).replace('[Chorus]',''))

data['text'] = data['text'].str.lower()

#print(data['text'].loc[8])
#print(data_orig['text'].loc[8])

#output_file1 = 'data/sd_withart.csv'
#data.to_csv(output_file1)

data['text']=data['text'].apply(lambda x:str(x).replace(' a ',' '))
data['text']=data['text'].apply(lambda x:str(x).replace(' an ',' '))
data['text']=data['text'].apply(lambda x:str(x).replace(' the ',' '))

#print(data['text'])
#print(data_orig['text'])

output_file2 = 'data/sd_withoutart.csv'
data.to_csv(output_file2)