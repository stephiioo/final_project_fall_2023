# final_project_fall_2023


## objective: to combine many of the tools and services explored over the semester and create any web service (product) that utilizes at least 10 of the 11 sections provided. 



## project details: this project involves the use of fake data to create and populate a website that displays information about patients (including: first and last name, date of birth, gender, and contact information) and medical records (including: patient id, diagnosis, treatment, admission date, and discharge date).



## technologies used:

### - Github (Version Control)
### - Flask (Python; Frotend & Backend) 
### - MySQL (Database via GCP)
### - SQLAlchemy (ORM) 
### - .ENV (Environment Variables) 
### - Tailwind (Frontend Styling)
### - Authorization (Google OAuth) 
### - API Service (Flask Backend) 
### - Logger and or Sentry.io (Debugging & Logging) 
### - Docker (Containerization) 
### - GCP (Deployment)

### .env
##### DB_HOST=34.27.105.165
##### DB_DATABASE=
##### DB_USERNAME=
##### DB_PASSWORD=
##### DB_PORT=3306
##### DB_CHARSET=utf8mb4
##### GOOGLE_CLIENT_ID = 
##### GOOGLE_CLIENT_SECRET = 

## Steps I took to run the app:

### make repo in github then clone it into cloud shell

### cd into the terminal

### install all your necessary requirements and create all your necessary folders and files

### create instance and cloud storage bucket (to save image) in gcp

### re-use/adjust codes from previous homeworks and follow the steps detailed in your previous readmes to assist with running the codes


### deploy web application on azure

### important commands:

### docker: 

#### steps:

##### 1. run 'docker' 
##### 2. run docker build -t final .
##### 3. docker run -p 8005:5000 final
##### 4. docker ps -> to run a container we already have
##### 5. docker stop -> to stop image


### deploying on gcp

##### gcloud config set project [YOUR_PROJECT_ID]
##### gcloud app deploy
#### to note: you may be prompted to chose a region when deploying




