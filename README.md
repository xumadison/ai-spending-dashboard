# AI-Powered Spending Insight Dashboard

Minimal scaffold. Start with health check and basic CSV analysis.

## Quickstart

```bash
# Build
docker build -t ai-spending-dashboard .

# Run
docker run --rm -p 8080:8080 --env-file .env.example ai-spending-dashboard

# Health
curl http://localhost:8080/health
```

## Analyze Endpoint

POST a CSV file with columns `Date,Merchant,Category,Amount` to `/analyze`:
```bash
curl -X POST -F "file=@assets/sample_data.csv" http://localhost:8080/analyze
```
