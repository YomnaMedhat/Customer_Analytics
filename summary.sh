#!/bin/bash
set -e

echo "------------------------------------------"
echo "  Telecom Churn Analytics Pipeline"
echo "------------------------------------------"

echo "Step 1: Ingesting Data..."
py ingest.py

echo "Step 2: Preprocessing..."
py preprocess.py

echo "Step 3: Clustering..."
py cluster.py

echo "Step 4: Analytics..."
py analytics.py

echo "Step 5: Visualizing..."
py visualize.py