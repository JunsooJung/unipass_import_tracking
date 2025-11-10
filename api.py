import requests
import pandas as pd
import xml.etree.ElementTree as ET


api_key = 'YOUR_API_KEY'
crt_num = 'YOUR_CERT_NUMBER'
url = "https://unipass.customs.go.kr:38010/ext/rest/cargCsclPrgsInfoQry/retrieveCargCsclPrgsInfo?crkyCn={api_key}&cargMtNo={crt_num}"

def fetch_data():
    response = requests.get(url.format(api_key=api_key, crt_num=crt_num))
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

