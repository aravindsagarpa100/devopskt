FROM python:3.9-slim-buster
WORKDIR /app
COPY /pythonapp /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]