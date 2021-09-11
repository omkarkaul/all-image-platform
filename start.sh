#!/bin/bash

pipenv shell
gunicorn -w 4 --bind 0.0.0.0:5000 --log-level=debug app:app