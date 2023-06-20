FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
RUN mkdir templates
COPY templates/*  /templates/
RUN chmod -R a+rwx templates
CMD ["python","app.py"]