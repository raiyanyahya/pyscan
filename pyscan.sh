#!/usr/bin/env bash

echo 'starting scan'
mkdir pyscan

echo "executing pylint-runner"
pylint_runner --disable C,R >> pyscan/pylint

echo "executing bandit"
bandit -r . -ii -ll -q  --format custom --msg-template "{relpath}:{line}: {confidence} {severity}: {msg}"  >> pyscan/bandit

echo "running flake8"
flake8 --filename=*.py --ignore=F405,F403,E501 --statistics >> pyscan/flake8

echo "running vulture"
vulture . --min-confidence 90 >> pyscan/vulture

echo "scan done"

python /tmp/reports.py