FROM python:3.12
WORKDIR /calc

COPY calc.py .

EXPOSE ${CALC_PORT:-13337}

# CMD ["python", "bs_server_III.py", "-p", ${PORT}]

CMD bash -c "python calc.py -p ${CALC_PORT}"
