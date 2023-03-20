import requests
import json

data = [5.1, 3.5, 1.4, 0.2]  # Example input data
payload = {'data': data}
response = requests.post('http://localhost:5000/predict', json=payload)

if response.ok:
    result = json.loads(response.text)
    print(result['prediction'])  # Should print 'setosa'
else:
    print('Error:', response.status_code, response.text)