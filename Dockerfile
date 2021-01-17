FROM python:3.7
WORKDIR /sizer-backend
ADD . /sizer-backend





# install requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000

ENV NAME OpentoAll

ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0