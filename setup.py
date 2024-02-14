import csv
import pandas as pd
import requests
    
    
url = f'https://api.github.com/repos/edomenico/edomenico/contents/metar_trat_teste2.csv?ref=main'
data = requests.get(url, headers={'Authorization': f'token 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', 'Accept': 'application/vnd.github.v3.raw'})    


    
    
with open('metar_trat_teste2.csv', 'w') as f: 
       
    f.write('k')
dff = pd.read_csv('metar_trat_teste2.csv')
print(dff)



# Define a function to create the search page
