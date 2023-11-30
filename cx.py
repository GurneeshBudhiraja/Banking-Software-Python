import csv
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
    postal_code=Customer.get_postal(name,postal_code)
    with open('cx.csv','r') as file:
      reader=csv.DictReader(file)
      for row in reader:
        if (row['name']==name and row['postal code']==postal_code):
          return row;
        else:
          pass
  
  @staticmethod
  def currency_rate():
    response=requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&symbols=CAD')
    api_output = response.json()
    rate = api_output['rates']['CAD']
    return rate
  
  @staticmethod
  def valid_postal(new_postal):
    pattern = re.compile('^[A-Za-z][0-9][A-Za-z][0-9][A-Za-z][0-9]$')
    if pattern.fullmatch(new_postal):
      return True
    
    return False

  @staticmethod
  def update_postal(name,postal_code,new_postal):
    dictionary_list=[]
    with open('cx.csv','r') as file:
      reader=csv.DictReader(file)
      for row in reader:
        dictionary_list.append(row)
    headers=list(dictionary_list[0]) #for extracting the headers from the list of dictionaries
    with open('cx.csv','w',newline='') as file:
      writer=csv.DictWriter(file,fieldnames=headers)
      writer.writeheader()
      for row in dictionary_list:
        if row['name']==name and row['postal code']==postal_code:
          row['postal code']=new_postal
        writer.writerow(row)
    return 0
  
  
  @staticmethod
  def get_postal(name,postal_code):
    with open('cx.csv','r') as file:
      reader=csv.DictReader(file)
      for row in reader:
        if (row['name']==name):
          return row['postal code'];
      return postal_code