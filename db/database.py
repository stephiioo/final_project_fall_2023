import logging
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

## configure logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/class.log",
    filemode="w",
    format='%(levelname)s - %(name)s - %(message)s'
)

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    contact_number = Column(String(15))

    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    doctor = relationship('Doctor', back_populates='patients')

    records = relationship('MedicalRecord', back_populates='patient')

class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True)
    doctor_name = Column(String(255))
    specialty = Column(String(255))

    patients = relationship('Patient', back_populates='doctor')

class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    diagnosis = Column(String(100), nullable=False)
    treatment = Column(String(200))
    admission_date = Column(Date, nullable=False)
    discharge_date = Column(Date)

    patient = relationship('Patient', back_populates='records')


if __name__ == "__main__":
    
    try:
        DATABASE_URL = "sqlite:///local.db"
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        logging.debug("Tables created successfully")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

   ## create connection and tables
# DATABASE_URL = "mysql+mysqlconnector://hants:sbu-admin-2023@scratch-server:3306/hants"