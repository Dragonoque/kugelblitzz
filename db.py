from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ClubMember(Base):
    __tablename__ = 'club_members'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    batch = Column(String)
    course = Column(String)
    phone = Column(String)
    email = Column(String)
    position = Column(String)
    picture = Column(LargeBinary)

engine = create_engine('sqlite:///club_members.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
