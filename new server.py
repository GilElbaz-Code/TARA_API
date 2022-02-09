from numpy import genfromtxt
from time import time
import pandas as pd
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def load_data(file_name):
    df = pd.read_csv('members.csv', index_col=False,)
    df.reset_index(drop=True, inplace=True)
    return df.values.tolist()


Base = declarative_base()


class Member(Base):
    # Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'Members'
    __table_args__ = {'sqlite_autoincrement': True}
    # tell SQLAlchemy the name of column and its attributes:
    member_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    party = Column(String)
    gov_role = Column(String)
    knesset_role = Column(String)
    additional_role = Column(String)
    party_role = Column(String)
    personal_phone = Column(Integer)
    office_phone = Column(Integer)
    email = Column(String)
    speaker_name = Column(String)
    speaker_phone = Column(Integer)
    head_office_name = Column(String)
    head_office_phone = Column(Integer)
    political_consultant_name = Column(String)
    political_consultant_phone = Column(Integer)
    picture = Column(String)
    position = Column(String)


if __name__ == "__main__":
    t = time()

    # Create the database
    engine = create_engine('sqlite:///knesset.db')
    Base.metadata.create_all(engine)

    # Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    file_name = "members.csv"
    data = load_data(file_name)

    for i in data:
        record = Member(**{
            'first_name': i[0],
            'last_name': i[1],
            'party': i[2],
            'gov_role': i[3],
            'knesset_role': i[4],
            'additional_role': i[5],
            'party_role': i[6],
            'personal_phone': i[7],
            'office_phone': i[8],
            'email': i[9],
            'speaker_name': i[10],
            'speaker_phone': i[11],
            'head_office_name': i[12],
            'head_office_phone': i[13],
            'political_consultant_name': i[14],
            'political_consultant_phone': i[15],
            'picture': i[16],
            'position': i[17]
        })
        s.add(record)  # Add all the records

    s.commit()  # Attempt to commit all the records
    s.close()  # Close the connection
