FROM python:3.10.16-slim-bullseye

ENV PYTHONDONTWRITEBYTECOD=1
ENV PYTHONUNBUDDERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD [ "sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn Django.wsgi:application --bind 0.0.0.0:8000" ]