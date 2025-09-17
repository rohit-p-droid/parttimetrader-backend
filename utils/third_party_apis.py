import os
import requests

def nse_ind_api(url):
    full_url = os.environ.get('NSE_IND') + url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.nseindia.com/",
    }
    resp = requests.get(full_url, headers=headers, timeout=5)
    print(resp)
    data = resp.json()
    return data

def bse_ind_api(url):
    full_url = os.environ.get('BSE_IND') + url
    resp = requests.get(full_url, timeout=5)
    data = resp.json()
    return data

def yahoo_finance_api(url):
    full_url = os.environ.get('YAHOO_FINANCE') + url
    resp = requests.get(full_url, timeout=5)
    data = resp.json()
    return data

def twelvedata_api(url):
    full_url = os.environ.get('TWELVE_DATA') + url
    print(full_url)
    params = {
        "exchange": "NSE",
        "apikey": 'TWELVE_DATA_API_KEY'
    }   
    resp = requests.get(full_url, params=params, timeout=5) 
    data = resp.json()
    return data






