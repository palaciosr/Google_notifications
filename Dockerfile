FROM python:3.7

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD['python',"google_auth.py"]