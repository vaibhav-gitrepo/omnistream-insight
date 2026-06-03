FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Run training script first to save the model, then start consumer
CMD ["bash", "-c", "python model_trainer.py && python consumer.py"]