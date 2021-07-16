FROM python:3.7-alpine
WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers
RUN python3 -m venv venv && source venv/bin/activate
RUN pip install twilio flask python-dotenv flask-cors
COPY . .
EXPOSE 3000
CMD ["python3", "main.py"]