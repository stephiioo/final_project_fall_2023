from flask import Flask, render_template, jsonify, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from database import Base, Patient, Doctor, MedicalRecord
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import logging
from db_functions import update_or_create_user

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(12)
oauth = OAuth(app)

## Database configuration
DATABASE_URL = "mysql+mysqlconnector://final:Finalproject1@34.27.105.165/root"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
Base.metadata.bind = create_engine(DATABASE_URL)

## Create a SQLAlchemy session
Session = sessionmaker(bind=Base.metadata.bind)
session = Session()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/app.log",
    filemode="w",
    format='%(levelname)s - %(name)s - %(message)s'
)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/')
def index():
    try:
        logging.debug("Success! Default endpoint accessed")
        return "Final project accomplished"
    except Exception as e:
        logging.error(f"An error occurred! {e}")
        return "Try again"

@app.route('/patients')
def display_patients():
    patients = session.query(Patient).all()
    return render_template('patients.html', patients=patients)

@app.route('/doctors')
def display_doctors():
    doctors = session.query(Doctor).all()
    return render_template('doctors.html', doctors=doctors)

@app.route('/medical_records')
def display_medical_records():
    medical_records = session.query(MedicalRecord).all()
    return render_template('medical_records.html', medical_records=medical_records)

## API endpoint to return sample data as JSON
@app.route('/api/data')
def get_sample_data():
    sample_data = {
        'message': 'This is to fulfill the API endpoint criteria',
        'details': 'The goal of this code is for the API endpoint to return the sample data as JSON'
    }
    logging.debug("API endpoint criteria fulfilled")
    return jsonify(sample_data)

# Google OAuth
GOOGLE_CLIENT_ID = '437210046789-b0fru5oi02e3svmnroigp84jbhvjhf02.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'

@app.route('/google/')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    redirect_uri = url_for('google_auth', _external=True)
    session['nonce'] = generate_token()
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    update_or_create_user(user)
    print(" Google User ", user)
    return redirect('/dashboard')

@app.route('/dashboard/')
def dashboard():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
