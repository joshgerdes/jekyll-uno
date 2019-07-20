FROM ruby:2.6

ADD . /app
WORKDIR /app
EXPOSE 4000

RUN ruby --version
RUN bundle install
CMD bundle exec jekyll serve --watch
