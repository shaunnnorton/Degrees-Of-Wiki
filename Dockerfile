FROM python:3.7-slim-buster

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN ls -a

ENV FLASK_APP=app.py
ENV FLASK_ENV=developement
ENV SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://ADMIN:maurice0012@srv-captain--wikidegrees-db-db:8080/default
ENV SECRET_KEY=8675309FRIDAY

EXPOSE 5000
 
CMD [ "python3", "-m","flask", "run", "--host=0.0.0.0" ]
