
FROM scrapinghub/scrapinghub-stack-scrapy:2.1

#============================================
# Firefox and Geckodriver
##============================================
#RUN apt-get update                             \
# && apt-get install -y --no-install-recommends \
#    ca-certificates curl firefox-esr           \
# && rm -fr /var/lib/apt/lists/*                \
# && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz | tar xz -C /usr/local/bin \
# && apt-get purge -y ca-certificates curl


ENV TERM xterm
ENV SCRAPY_SETTINGS_MODULE scrapy_fb.settings
RUN mkdir -p /app
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
RUN python setup.py install

