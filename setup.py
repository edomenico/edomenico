import csv
import pandas as pd
import requests
    
    
url = f'https://api.github.com/repos/edomenico/edomenico/contents/escala1050.xlsx?ref=main'
data = requests.get(url, headers={'Authorization': f'token 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', 'Accept': 'application/vnd.github.v3.raw'})    
#url = f'https://api.github.com/repos/edomenico/edomenico/contents/escala1050.xlsx?ref=main'
#data = requests.get(url, headers='Authorization': f'token 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', 'Accept': 'application/vnd.github.v3.raw')

    
    
with open('test_excel.xlsx', 'wb') as f: 
       
    f.write(data.content)
dff = pd.read_excel('test_excel.xlsx')
print(dff)



# Define a function to create the search page
