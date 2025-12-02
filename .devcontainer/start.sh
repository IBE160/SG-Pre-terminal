#!/bin/bash
set -e

echo "--- Starting backend service ---"
cd /workspace/excelence/backend
uvicorn main:app --host 0.0.0.0 --port 8000 &
echo "Backend started on port 8000"

echo "--- Starting frontend service ---"
cd /workspace/excelence/frontend
npm run dev -- --host 0.0.0.0 --port 5173 &
echo "Frontend started on port 5173"

echo "--- Dev container is ready ---"
