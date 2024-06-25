FROM python

WORKDIR /app

COPY jogoBatalha.py /app

COPY requirements.txt /app/

RUN apt-get update

RUN apt-get install nano

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "jogoBatalha.py"]