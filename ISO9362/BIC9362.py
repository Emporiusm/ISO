# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import os
# %%
filedir = os.getcwd() + '/'
jsondir = filedir + 'AllCountries' + '/'
filelist = os.listdir(jsondir)
files = [jsondir + file for file in filelist if (file.endswith('.json') and len(file) == 7)]

df = pd.DataFrame()
for file in files:
    with open(file,'r') as content:
        text = content.read()
        jframe = pd.read_json(text)
        df = df.append(jframe)
df = df.reset_index(drop=True)

tempjson = filedir + 'list.json'
tmpjs = df['list'].to_json(
    tempjson,
    orient='columns'
)

lframe = pd.read_json(tempjson,orient='index')
os.remove(tempjson)
lframe = lframe.reset_index(drop=True)
frame = df.join(lframe)
frame = frame.filter(items=['country_code','country','bank','city','branch','swift_code'])
frame.to_csv(filedir + 'ISO9362 complete.csv')
exit


