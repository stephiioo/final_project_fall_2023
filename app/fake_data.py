from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Patient, MedicalRecord, Base
from datetime import datetime  # Import datetime module

# MySQL database connection
DATABASE_URL = "mysql+mysqlconnector://steph:Finalproject1@34.27.105.165/steph"  
engine = create_engine(DATABASE_URL)

# Bind the engine to the base
Base.metadata.bind = engine

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to get manual input for patient data
def get_patient_input():
    patients_data = [
        {"first_name": "John", "last_name": "Doe", "date_of_birth": datetime(1980, 5, 15), "gender": "Male", "contact_number": "1234567890"},
        {"first_name": "Jane", "last_name": "Smith", "date_of_birth": datetime(1992, 8, 21), "gender": "Female", "contact_number": "9876543210"},
        {"first_name": "James", "last_name": "Matthew", "date_of_birth": datetime(2000, 4, 12), "gender": "Female", "contact_number": "6316321316"},
        {"first_name": "Jung", "last_name": "Seowoon", "date_of_birth": datetime(1999, 7, 2), "gender": "Male", "contact_number": "6316324999"},
        {"first_name": "Rose", "last_name": "Justin", "date_of_birth": datetime(2001, 5, 18), "gender": "Male", "contact_number": "8444567890"},
        {"first_name": "Aria", "last_name": "Cone", "date_of_birth": datetime(1992, 8, 21), "gender": "Female", "contact_number": "9814543200"},
        {"first_name": "Kim", "last_name": "Woobin", "date_of_birth": datetime(1990, 1, 15), "gender": "Male", "contact_number": "6331117890"},
        {"first_name": "Lane", "last_name": "Kathy", "date_of_birth": datetime(1992, 8, 21), "gender": "Female", "contact_number": "9817243220"},
        {"first_name": "John", "last_name": "Jean", "date_of_birth": datetime(2005, 9, 10), "gender": "Male", "contact_number": "5164560700"},
        {"first_name": "Patricia", "last_name": "Perry", "date_of_birth": datetime(1974, 3, 11), "gender": "Female", "contact_number": "6376599211"}
    ]

    patients = []
    for data in patients_data:
        patient = Patient(
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth'],
            gender=data['gender'],
            contact_number=data['contact_number']
        )
        patients.append(patient)

    return patients

# Function to get manual input for medical record data
def get_medical_record_input(patient):
    medical_records_data = [
        {"diagnosis": "Insomnia", "treatment": "Melatonin", "admission_date": "2023-01-01", "discharge_date": "2023-01-10"},
        {"diagnosis": "Headache", "treatment": "Tylenol", "admission_date": "2023-01-01", "discharge_date": "2023-01-03"},
        {"diagnosis": "Cancer", "treatment": "Chemotherapy", "admission_date": "2023-01-04", "discharge_date": "2023-12-17"},
        {"diagnosis": "Bipolar I", "treatment": "Lithium", "admission_date": "2023-02-07", "discharge_date": "2023-02-27"},
        {"diagnosis": "Dehydration", "treatment": "IV", "admission_date": "2023-12-15", "discharge_date": "2023-12-17"},
        {"diagnosis": "Stomachache", "treatment": "Tums", "admission_date": "2023-12-16", "discharge_date": "2023-12-16"},
        {"diagnosis": "Astigmatism", "treatment": "Glasses", "admission_date": "2023-12-17", "discharge_date": "2023-12-17"},
        {"diagnosis": "Cardiovascular Disease", "treatment": "Cardiac Bypass", "admission_date": "2023-02-01", "discharge_date": "2023-02-10"},
        {"diagnosis": "Stomach Pain", "treatment": "Tums", "admission_date": "2023-12-17", "discharge_date": "2023-12-17"},
        {"diagnosis": "Headache", "treatment": "Aspirin", "admission_date": "2023-012-01", "discharge_date": "2023-12-02"},
    ]

    medical_records = []
    for data in medical_records_data:
        medical_record = MedicalRecord(
            patient=patient,
            diagnosis=data['diagnosis'],
            treatment=data['treatment'],
            admission_date=data['admission_date'],
            discharge_date=data['discharge_date']
        )
        medical_records.append(medical_record)

    return medical_records

# Insert manual data for patients and their medical records
patients = get_patient_input()
for patient in patients:
    session.add(patient)
    session.commit()
    medical_records = get_medical_record_input(patient)
    for medical_record in medical_records:
        session.add(medical_record)
        session.commit()

# Close the session
session.close()

print("Done")
