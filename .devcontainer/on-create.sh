#!/bin/bash
set -e

echo "--- Installing backend dependencies ---"
cd /workspace/excelence/backend
uv pip install -e .

echo "--- Installing frontend dependencies ---"
cd /workspace/excelence/frontend
npm install

echo "--- Dependency installation complete ---"
