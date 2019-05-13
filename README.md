# Django with Wagtail and WebPack Cookiecutter

An opinionated [Cookiecutter](https://github.com/audreyr/cookiecutter) template for
creating Django projects with Wagtail and Webpack.


## Features

Ready to be used with:
* Wagtail
* Django Webpack Loader
* Django Debug Toolbar
* Heroku
* PostgreSQL
* Docker (with [Docker for Django Cookiecutter](https://github.com/jmfederico/cookiecutter-django-docker))

It comes configured with:
* A custom user model that extends the base Django user model.
* Superuser authentication with credentials stored in environmental variables.


## Requirements

* [Poetry](https://poetry.eustace.io)
* [NPM](https://docs.npmjs.com)


## Usage

```bash
# Bake cookie!
cookiecutter gh:jmfederico/cookiecutter-django
```

```bash
# Setup python project
poetry init
# Install python dependencies
poetry add \
    django \
    psycopg2 \
    wagtail \
    django_webpack_loader \
    django_debug_toolbar \
    django_heroku \
    gunicorn
```

```bash
# Install node dependencies
npm add -D \
    @babel/core \
    @babel/preset-env \
    autoprefixer \
    babel-loader \
    clean-webpack-plugin \
    clean-webpack-plugin \
    css-loader \
    cssnano \
    event-hooks-webpack-plugin \
    file-loader \
    mini-css-extract-plugin \
    node-sass \
    nucleus-styleguide \
    optimize-css-assets-webpack-plugin \
    postcss-loader \
    sass-loader \
    source-map-loader \
    style-loader \
    url-loader \
    webpack \
    webpack-bundle-tracker \
    webpack-cli \
    webpack-plugin-serve
```

```bash
# Automatically generate dotenv files
docker run --rm -v "`pwd`:/var/lib/dotenver/" jmfederico/dotenver

# Take a look to the generated dotenv (.env) file, and modify to your needs.
```

```bash
# Build docker images
docker-compose build
```

```bash
# Make migrations
docker-compose run --rm django ./manage.py makemigrations
```

```bash
# Run your project
docker-compose up -d
```

Visit https://localhost/admin/
