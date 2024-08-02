FROM python:3.9
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=run.py
CMD ["flask", "run", "--host=0.0.0.0"]