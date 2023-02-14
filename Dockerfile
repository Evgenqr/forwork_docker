    FROM python:3.9.4

    RUN apt-get update && apt-get install -y \
        build-essential \
        libpq-dev \
        python3-dev \
        postgresql-client
        
    WORKDIR /app

    COPY requirements.txt .

    RUN pip install -r requirements.txt


    COPY . .

    EXPOSE 8000

    ENTRYPOINT [ "./docker-entrypoint.sh" ]

    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]