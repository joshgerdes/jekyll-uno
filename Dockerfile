FROM ruby:slim

LABEL Name=jmuelbertgithub Version=0.0.1

EXPOSE 3000

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

WORKDIR /app
COPY . /app

COPY Gemfile Gemfile.lock ./
RUN bundle install

CMD ["ruby", "jmuelbertgithub.rb"]
