#!/bin/bash
PYTHON_SCRIPT='solution-1.py'
INTERVAL=10

echo "staring the log checker.Press Ctrl+C for termination"

while true
do
    echo "running the python script to check for errors"
    python3 "$PYTHON_SCRIPT"
    echo "Explicitely sleeping for interval seconds"
    sleep $INTERVAL
done
