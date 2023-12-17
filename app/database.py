import logging
from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
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

    records = relationship('MedicalRecord', back_populates='patient')

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
        DATABASE_URL = "mysql+mysqlconnector://steph:Finalproject1@34.27.105.165/steph"
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        logging.debug("Tables created successfully")
        
        # test connection and print table names
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        logging.debug(f"Tables in the database: {table_names}")
        print("Tables in the database:", table_names)
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
