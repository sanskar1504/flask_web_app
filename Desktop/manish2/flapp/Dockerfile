FROM python:alpine3.7
EXPOSE 5000   
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 

CMD [ "python","crud.py" ] 
