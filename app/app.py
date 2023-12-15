from flask import Flask, render_template, jsonify
from db import Base, Patient, Doctor, MedicalRecord
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Database configuration
DATABASE_URL = "sqlite:///local.db"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
Base.metadata.bind = app

# Create a SQLAlchemy engine and session
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    return render_template('index.html')

# Route to display patients
@app.route('/patients')
def display_patients():
    patients = session.query(Patient).all()
    return render_template('patients.html', patients=patients)

# Route to display doctors
@app.route('/doctors')
def display_doctors():
    doctors = session.query(Doctor).all()
    return render_template('doctors.html', doctors=doctors)

# Route to display medical records
@app.route('/medical_records')
def display_medical_records():
    medical_records = session.query(MedicalRecord).all()
    return render_template('medical_records.html', medical_records=medical_records)

# API endpoint to return sample data as JSON
@app.route('/api/data')
def get_sample_data():
    sample_data = {
        'message': 'This is to fulfill the API endpoint criteria',
        'details': 'The goal of this code is for the API endpoint to return the ssample data as JSON'
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)
