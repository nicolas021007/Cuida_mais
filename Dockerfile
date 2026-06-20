FROM  python:3.9-slim
WORKDIR /src/app

COPY . /src/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]