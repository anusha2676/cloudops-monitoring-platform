from fastapi import FastAPI

app = FastAPI(
title="CloudOps Monitoring Platform",
description="Cloud monitoring and auto-healing platform",
version="1.0.0"
)

@app.get("/")
def home():
return {
"message": "CloudOps Monitoring Platform is running",
"status": "healthy"
}

@app.get("/health")
def health_check():
return {
"status": "healthy"
}
