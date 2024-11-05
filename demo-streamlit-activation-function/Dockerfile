FROM python:3.10
WORKDIR /app/

COPY . /app/
RUN pip install -r requirements.txt

EXPOSE 8501
CMD ["python", "-m", "streamlit", "run", "app.py"]
