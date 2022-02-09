import pandas as pd

raw = pd.read_excel('kms.xlsx')
raw_csv = raw.to_csv('members.csv')

print(raw_csv)

#json_file = raw.to_json(force_ascii=False, orient='records')

data = [
    {
        "member_name": "Jimmy",
        "party": "Something",
        "gov_role": "Head of..",
        "knesset_role": "knesset_role",
        "additional_role": "commitee",
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
        "picture": "sdas",
        "position": "coalition"
    }
]


