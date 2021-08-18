# Before running this program - 
# Install pandas and openpyxl
# pip install panadas 
# pip install openpyxl


import pandas as pd

data = pd.read_json("https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog")

# if index is not set to false then in the excel file there will be an extra unnamed column representing index
data.to_excel("result.xlsx", index=False)