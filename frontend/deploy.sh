#!/usr/bin/env sh

# Abort on errors
set -e

# Build the frontend
yarn run build

# navigate into the build output directory
cd dist

git init
git add -A
git commit -m 'deploy'

git push -f git@github.com:rbazin/eco-eco-app.git main:gh-pages

cd -