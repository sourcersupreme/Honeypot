#!/bin/bash

echo "[*] Starting Honeypot..."
python3 honeypot/server.py &

echo "[*] Starting Dashboard..."
cd dashboard
python3 app.py
