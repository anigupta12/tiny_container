# Getting the python image
FROM python:3.7

LABEL Creator="animesh"
LABEL Purpose="analyze_sequence"

WORKDIR /analyze_sequence

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

COPY get_base_counts.py ./
RUN python3 get_base_counts.py