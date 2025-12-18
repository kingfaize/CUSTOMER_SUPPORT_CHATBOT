# GCP Cloud Run Deployment Guide for CUSTOMER_SUPPORT_CHATBOT

## Prerequisites
- Google Cloud account and project
- gcloud CLI installed and authenticated
- Billing enabled for your project
- Docker installed locally

## 1. Enable Required APIs
```
gcloud services enable run.googleapis.com artifactregistry.googleapis.com
```

## 2. Build and Push Docker Image
Replace `[PROJECT_ID]` and `[REGION]` with your GCP project and region.

```
# Set variables
PROJECT_ID="your-gcp-project-id"
REGION="us-central1"
REPO="customer-support-chatbot"

# Create Artifact Registry repo (if not exists)
gcloud artifacts repositories create $REPO --repository-format=docker --location=$REGION

# Authenticate Docker to Artifact Registry
gcloud auth configure-docker $REGION-docker.pkg.dev

# Build Docker image
docker build -t $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/chatbot:latest .

# Push image to Artifact Registry
docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/chatbot:latest
```

## 3. Deploy to Cloud Run
```
gcloud run deploy chatbot \
  --image $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/chatbot:latest \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --port 8080
```

## 4. Set Environment Variables
If you use a `.env` file, set these as Cloud Run environment variables:
- `OPENAI_API_KEY`
- `MCP_SERVER_URL`
- Any other secrets

Example:
```
gcloud run services update chatbot \
  --update-env-vars OPENAI_API_KEY=your-key,MCP_SERVER_URL=your-url \
  --region $REGION
```

## 5. Access Your App
After deployment, Cloud Run will provide a public URL for your chatbot.

---

For more details, see: https://cloud.google.com/run/docs/deploying
