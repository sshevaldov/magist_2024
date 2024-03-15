import json
import requests

url = 'http://plans.athene.tech/rest/get-inference'
headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
}

age = 65
income = 20000

data = {
    "inputVariables": [
        {
            "name": "возраст",
            "values": [
                {
                    "fuzzyTerm": "молодой",
                    "value": 35
                },
                {
                    "fuzzyTerm": "средний",
                    "value": 45
                },
                {
                    "fuzzyTerm": "старый",
                    "value": 65
                }]
        },
        {
            "name": "доход",
            "values": [
                {
                    "fuzzyTerm": "низкий",
                    "value": 50000
                },
                {
                    "fuzzyTerm": "средний",
                    "value": 100000
                },
                {
                    "fuzzyTerm": "высокий",
                    "value": 500000
                }]
        }],
    "outputVariable":
        {
            "name": "кредит",
            "values": [
                {
                    "fuzzyTerm": "небольшой",
                    "value": 50000
                },
                {
                    "fuzzyTerm": "средний",
                    "value": 100000
                },
                {
                    "fuzzyTerm": "большой",
                    "value": 200000
                }]
        },
    "rules": [
        "if доход is высокий and возраст is молодой then кредит is большой",
        "if доход is высокий and возраст is средний then кредит is средний",
        "if доход is высокий and возраст is старый then кредит is средний",
        "if доход is низкий and возраст is молодой then кредит is небольшой"
    ],
    "values":
        {
            "доход": income,
            "возраст": age
        }
}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.json())
