from sqlalchemy import Column, Integer, String
from database import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(100), nullable=False)
    technology_data = Column(String(500), nullable=False)

    @property
    def technologies(self):
        return self.technology_data.split(", ")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=False)
    technology_data = Column(String(500), nullable=False)
    github = Column(String(500), default="")

    @property
    def technologies(self):
        return self.technology_data.split(", ")


class Certification(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    organization = Column(String(150), nullable=False)
    date = Column(String(50), default="")
    credential = Column(String(500), default="")


class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    subject = Column(String(200), nullable=False)
    message = Column(String(2000), nullable=False)
