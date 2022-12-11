FROM x0rzkov/twint:latest

RUN pip3 install pipenv
RUN pipenv install git+https://github.com/twintproject/twint.git#egg=twint
RUN pipenv run pip3 install python-telegram-bot googletrans==3.1.0a0

COPY run.py ./
COPY config.txt ./

ENTRYPOINT ["/bin/bash"]

# CMD ["/usr/bin/tail", "-f /dev/null"] # keep run forever