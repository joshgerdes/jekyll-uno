# Jekyll-Uno
> A minimal, responsive theme for Jekyll based on the [Uno](https://github.com/daleanthony/Uno) theme for Ghost

[![Made with Ruby](https://img.shields.io/badge/Ruby->=2.6-blue?logo=ruby&logoColor=white)](https://ruby-lang.org)
[![Made for Jekyll](https://img.shields.io/badge/Jekyll-3.9-blue?logo=jekyll&logoColor=white)](https://jekyllrb.com)

## Features

* Clean layout
* Resposive layout
* Pagination
* Syntax highlighting
* Social links
* Tags listing page
* Categories listing page
* Google Analytics integration
* Disqus integration

## Install system dependencies

1. Install Ruby - using your system's package manager or download from [Ruby Downloads](https://www.ruby-lang.org/en/downloads/).
2. Install Bundler if not installed already.
    ```sh
    gem install bundler
    ```

## Set up and run

1. Clone the repo, or [Download](https://github.com/joshgerdes/jekyll-uno/archive/master.zip) code from `master`.
    ```sh
    git clone git@github.com:joshgerdes/jekyll-uno.git
    cd jekyll-uno/
    ```
2. Install Ruby gems:
    ```sh
    bundle config set --local path vendor/bundle
    bundle install
    ```
3. Start the Jekyll dev server:
    ```sh
    bundle exec jekyll serve --trace
    ```

Open the browser at:

- [localhost:4000/jekyll-uno/](http://localhost:4000/jekyll-uno/)

If you would like to run without using the `github-pages` gem, update your `Gemfile` to the following:

```ruby
source 'https://rubygems.org'

gem 'jekyll', '~> 3.9'
gem 'kramdown'
gem 'kramdown-parser-gfm'

group :jekyll_plugins do
  gem 'jekyll-paginate'
  gem 'jekyll-watch'
end
```

## Demo

View demo at [joshgerdes.com/jekyll-uno/](https://joshgerdes.com/jekyll-uno/).

![jekyll-uno - free Jekyll theme](/screenshot.png)

## Copyright and license

Licensed under [MIT](/LICENSE) by [@joshgerdes](https://github.com/joshgerdes/jekyll-uno).
