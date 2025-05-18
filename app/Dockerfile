FROM python:3.9-slim

WORKDIR /app


COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 9000

CMD ["flask", "run", "--host=0.0.0.0", "--port=9000", "--reload"]

