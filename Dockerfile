FROM python:3.8

MAINTAINER scaryfase1237373@gmail.com

WORKDIR /home/dmitry/WildBot/
COPY . /home/dmitry/WildBot/
ENV TOKEN=""
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]