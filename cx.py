import csv #csv file
import requests  #for API
#env
import os 
from dotenv import load_dotenv  
#regular expression
import re 


load_dotenv()
api_key = os.getenv('api_key')


class Customer:
  @staticmethod
  def verified(name,postal_code):
    with open('cx.csv','r') as file:
      reader=csv.DictReader(file)
      for row in reader:
        if (row['name']==name and row['postal code']==postal_code):
          if (row['status']=='Active'):
            return ('active')
          else:
            return ('not_active')
      return ('not_found')
  
  @staticmethod
  def accountsummary(name,postal_code):
    with open('cx.csv','r') as file:
      reader=csv.DictReader(file)
      for row in reader:
        if (row['name']==name and row['postal code']==postal_code):
          return row;
        else:
          pass
  
  @staticmethod
  def currency_rate(name,postal_code):
    response=requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&symbols=CAD')
    api_output = response.json()
    rate = api_output['rates']['CAD']
    return rate
  
  @staticmethod
  def valid_postal(new_postal):
    pattern = re.compile('^[A-Za-z][0-9][A-Za-z][0-9][A-Za-z][0-9]$')
    if not pattern.fullmatch(new_postal):
      return False
    
    return True

  @staticmethod
  def update_postal(name,postal_code,new_postal):
    ...