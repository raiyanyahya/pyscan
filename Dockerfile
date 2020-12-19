FROM python:3.8-slim
COPY requirements.txt pyscan.sh reports.py /tmp/
RUN apt update -y \
    && pip install -r /tmp/requirements.txt \
    && chmod +x /tmp/hedvig.sh \
    && chmod +x /tmp/reports.py
WORKDIR /workdir
ENTRYPOINT ["/tmp/pyscan.sh"]
CMD [""]