FROM python:3.12
WORKDIR /chat

COPY chat.py .

EXPOSE ${CHAT_PORT:-3000}
EXPOSE ${MAX_USERS:-10}

CMD bash -c "python chat.py -p ${CHAT_PORT} -m ${MAX_USERS}"