import requests
import json

url = "http://environment.techlive.vn/Flight/Search"

payload = {
    "Adt": 1,
    "Chd": 0,
    "Inf": 0,
    "System": "VJA",
    "ListFlight": [
        {
            "Leg": 0,
            "StartPoint": "ICN",
            "EndPoint": "SGN",
            "DepartDate": "05102024"
        },
        {
            "Leg": 1,
            "StartPoint": "SGN",
            "EndPoint": "ICN",
            "DepartDate": "09112024"
        }

    ],
    "MemberUser": "",
    "HeaderUser": "TechLive",
    "HeaderPass": "EVHLt5gvLc6GN6p",
    "AgentCode": "KAO1609",
    "ProductKey": "lxce8dfo0qecglc",
}


headers = {
    "Content-Type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.headers)
print(response.json())

with open("response_output_vj_kaos.txt", "w") as file:
    file.write(f"Status Code: {response.status_code}\n")
    file.write(f"Headers: {json.dumps(dict(response.headers), indent=4)}\n")
    file.write(f"JSON Response: {json.dumps(response.json(), indent=4)}\n")