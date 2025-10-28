import requests

url = "http://localhost:9696/predict"


client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client)

sub_rate = response.json()

print('response = ', sub_rate)

if sub_rate['sub_probability'] >= 0.5:
    print('This client will get a subscription')
else:
    print('This client will not get a subscription')
