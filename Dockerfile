FROM python:3.9
WORKDIR /SelfBot
COPY requirements.txt /SelfBot/
RUN pip install -r requirements.txt
COPY . /SelfBot
CMD python main.py
