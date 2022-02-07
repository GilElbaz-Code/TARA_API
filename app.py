from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knesset.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Member(db.Model):
    # Auto increment by default
    member_id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(100), nullable=False)
    party = db.Column(db.String(100))
    gov_role = db.Column(db.String(255))
    knesset_role = db.Column(db.String(255))
    party_role = db.Column(db.String(255))
    personal_phone = db.Column(db.Integer)
    office_phone = db.Column(db.Integer)
    email = db.Column(db.String(255))
    speaker_name = db.Column(db.String(100))
    speaker_phone = db.Column(db.Integer)
    head_office_name = db.Column(db.String(100))
    head_office_phone = db.Column(db.Integer)
    political_consultant_name = db.Column(db.String(100))
    political_consultant_phone = db.Column(db.Integer)
    picture = db.Column(db.String(255))

    def __init__(self, member_name, party, gov_role, knesset_role, party_role, personal_phone, office_phone, email,
                 speaker_name, speaker_phone, head_office_name, head_office_phone, political_consultant_name,
                 political_consultant_phone, picture):
        self.member_name = member_name
        self.party = party
        self.gov_role = gov_role
        self.knesset_role = knesset_role
        self.party_role = party_role
        self.personal_phone = personal_phone
        self.office_phone = office_phone
        self.email = email
        self.speaker_name = speaker_name
        self.speaker_phone = speaker_phone
        self.head_office_name = head_office_name
        self.head_office_phone = head_office_phone
        self.political_consultant_name = political_consultant_name
        self.political_consultant_phone = political_consultant_phone
        self.picture = picture


class KnessetSchema(ma.Schema):
    class Meta:
        fields = (
            'member_id', 'member_name', 'party', 'gov_role', 'knesset_role', 'party_role', 'personal_phone',
            'office_phone', 'email',
            'speaker_name', 'speaker_phone', 'head_office_name', 'head_office_phone', 'political_consultant_name',
            'political_consultant_phone', 'picture')


member_schema = KnessetSchema()  # One
members_schema = KnessetSchema(many=True)  # Many


# Add member row
@app.route('/member', methods=['POST'])
def add_member():
    member_name = request.json['member_name']
    party = request.json['party']
    gov_role = request.json['gov_role']
    knesset_role = request.json['knesset_role']
    party_role = request.json['party_role']
    personal_phone = request.json['personal_phone']
    office_phone = request.json['office_phone']
    email = request.json['email']
    speaker_name = request.json['speaker_name']
    speaker_phone = request.json['speaker_phone']
    head_office_name = request.json['head_office_name']
    head_office_phone = request.json['head_office_phone']
    political_consultant_name = request.json['political_consultant_name']
    political_consultant_phone = request.json['political_consultant_phone']
    picture = request.json['picture']

    new_member = Member(member_name, party, gov_role, knesset_role, party_role, personal_phone, office_phone, email,
                        speaker_name, speaker_phone, head_office_name, head_office_phone, political_consultant_name,
                        political_consultant_phone, picture)

    db.session.add(new_member)
    db.session.commit()

    return member_schema.jsonify(new_member)


# Get All Members
@app.route('/member', methods=['GET'])
def get_members():
    all_members = Member.query.all()
    result = members_schema.dump(all_members)
    return jsonify(result.data)


# Get Single Member
@app.route('/member/<id>', methods=['GET'])
def get_product(member_id):
    member = Member.query.get(member_id)
    return member_schema.jsonify(member)


# Update a Member
@app.route('/member/<id>', methods=['PUT'])
def update_member(member_id):
    member = Member.query.get(member_id)

    member_name = request.json['member_name']
    party = request.json['party']
    gov_role = request.json['gov_role']
    knesset_role = request.json['knesset_role']
    party_role = request.json['party_role']
    personal_phone = request.json['personal_phone']
    office_phone = request.json['office_phone']
    email = request.json['email']
    speaker_name = request.json['speaker_name']
    speaker_phone = request.json['speaker_phone']
    head_office_name = request.json['head_office_name']
    head_office_phone = request.json['head_office_phone']
    political_consultant_name = request.json['political_consultant_name']
    political_consultant_phone = request.json['political_consultant_phone']
    picture = request.json['picture']

    member.member_name = member_name
    member.party = party
    member.gov_role = gov_role
    member.knesset_role = knesset_role
    member.party_role = party_role
    member.personal_phone = personal_phone
    member.office_phone = office_phone
    member.email = email
    member.speaker_name = speaker_name
    member.speaker_phone = speaker_phone
    member.head_office_name = head_office_name
    member.head_office_phone = head_office_phone
    member.political_consultant_name = political_consultant_name
    member.political_consultant_phone = political_consultant_phone
    member.picture = picture

    db.session.commit()

    return member_schema.jsonify(member)


# Delete Product
@app.route('/member/<id>', methods=['DELETE'])
def delete_product(member_id):
    member = Member.query.get(member_id)
    db.session.delete(member)
    db.session.commit()

    return member_schema.jsonify(member)


if __name__ == "__main__":
    app.run(debug=True)
