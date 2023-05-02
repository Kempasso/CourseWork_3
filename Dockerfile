FROM python:3.10

COPY requirements.txt /CourseWork_3/
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /CourseWork_3/requirements.txt

COPY . /CourseWork_3/
WORKDIR /CourseWork_3

EXPOSE 8000

CMD ["python3.10", "app.py"]
