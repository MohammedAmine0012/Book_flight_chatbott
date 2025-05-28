FROM rasa/rasa-sdk:3.6.2

USER root

RUN pip install requests

COPY actions /app/actions

USER 1001 