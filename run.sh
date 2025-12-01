#!/usr/bin/env bash
set -euo pipefail

IMAGE=ai-spending-dashboard

docker build -t ${IMAGE} .
docker run --rm -p 8080:8080 --env-file .env.example ${IMAGE}
