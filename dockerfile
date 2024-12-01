FROM python:3.9-slim


WORKDIR /app


COPY ./app /app


RUN pip install --no-cache-dir -r /app/requirements.txt


CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

