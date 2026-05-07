FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY sysmon.py .

EXPOSE 9090

CMD ["python", "sysmon.py"]
