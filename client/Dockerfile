# client.Dockerfile
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py migrate 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
