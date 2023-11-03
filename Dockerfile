FROM python:3.10

ENV PYTHONUNBUFFERED True
ENV APP_HOME /APP_HOME

WORKDIR $APP_HOME
COPY . ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]