FROM python:3.7-alpine
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 5050
CMD ["python", "app.py"]