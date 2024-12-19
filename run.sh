#!/bin/bash
# run.sh

# Start app.py for media management app on port 4000
python3 -m flask run --app management.app --port 4000 &

# Start the existing app on port 5000
python3 -m flask run --app DASHBOARD.app --port 5000
