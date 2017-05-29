import pandas as pd
import gzip

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    print d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

fullMetaAutomobile = getDF("path\\meta_Automobile.json.gz")

metaAutomobile = fullMetaAutomobile['asin','price','rating','title','overall']

metaAutomobile.to_csv("path\\meta_Automobile.csv",index = False)