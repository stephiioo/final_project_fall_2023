from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from database import Patient, Doctor, MedicalRecord
import random
from datetime import timedelta

# Create a SQLite database in the current working directory
DATABASE_URL = "mysql+mysqlconnector://final:Finalproject1@34.27.105.165/root"
engine = create_engine(DATABASE_URL)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a Faker instance
fake = Faker()

# Function to generate fake doctor data
def create_fake_doctor():
    return Doctor(
        doctor_name=fake.name(),
        specialty=fake.job()
    )

# Function to generate fake patient data
def create_fake_patient():
    return Patient(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        date_of_birth=fake.date_of_birth(),
        gender=random.choice(['Male', 'Female']),
        contact_number=fake.phone_number()
    )

# Function to generate fake medical record data
def create_fake_medical_record(patient):
    admission_date = fake.date_between(start_date='-30d', end_date='today')
    discharge_date = admission_date + timedelta(days=random.randint(1, 15))
    return MedicalRecord(
        patient=patient,
        diagnosis=fake.sentence(nb_words=5),
        treatment=fake.paragraph(),
        admission_date=admission_date,
        discharge_date=discharge_date if random.choice([True, False]) else None
    )

# Generate and insert fake data for doctors
for _ in range(50):  
    fake_doctor = create_fake_doctor()
    session.add(fake_doctor)
    session.commit()

# Generate and insert fake data for patients and their medical records
for _ in range(50): 
    fake_patient = create_fake_patient()
    session.add(fake_patient)
    session.commit()
    
    fake_medical_record = create_fake_medical_record(fake_patient)
    session.add(fake_medical_record)
    session.commit()

# Close the session
session.close()

print("Done")