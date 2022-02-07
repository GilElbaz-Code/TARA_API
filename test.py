import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {
        "member_name": "Jimmy",
        "party": "Something",
        "gov_role": "Head of..",
        "knesset_role": "knesset_role",
        "party_role": "party_role",
        "personal_phone": 555,
        "office_phone": 3242,
        "email": " gil@",
        "speaker_name": "jorge",
        "speaker_phone": 2321,
        "head_office_name": "sdas",
        "head_office_phone": 231,
        "political_consultant_name": "sdas",
        "political_consultant_phone": 2312,
        "picture": "sdas"
    }
]

for i in range(len(data)):
    response = requests.post(f'{BASE}/Member/{str(i)}', data[i])
    print(response.json())
