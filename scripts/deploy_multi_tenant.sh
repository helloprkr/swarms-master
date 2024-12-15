#!/bin/bash

echo "🚀 Deploying Multi-Tenant Swarms..."

# Ensure environment variables are set
if [ -z "$VERCEL_TOKEN" ]; then
    echo "❌ VERCEL_TOKEN not set"
    exit 1
fi

# Install dependencies
pip install -r requirements.txt

# Setup tenants
python scripts/manage_tenants.py

# Deploy to Vercel
vercel deploy --prod

echo "✅ Deployment complete!" 