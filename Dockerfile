FROM python:3.8-buster
WORKDIR /app
#COPY requirement.txt /app/
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Flask
COPY . /app/
EXPOSE 5000

#ENV FLASK_APP=app.py
#ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run", "--host=0.0.0.0"]
