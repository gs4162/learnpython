# imnports 
import datetime as dt

import pandas as pd

files = ['January.xlsx', 'February.xlsx', 'March.xlsx']
combined = pd.DataFrame()

for file in files:
    df = pd.read_excel(file)
    df[]
    combined = combined.append(df,ignore_index = True)
    
combined.to_excel('Sales_1Q20206969.xlsx', index = False, sheet_name='1q 2020 6969 sales') 
