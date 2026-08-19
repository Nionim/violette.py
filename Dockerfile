FROM python:3.11
WORKDIR /vio
COPY . /vio
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./violette.py"]