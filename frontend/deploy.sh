#!/bin/bash

set -e

# Build the frontend
yarn build

# navigate into the build output directory
cd dist

git init
git add -A
git commit -m 'deploy'

git push -f git@github.com:rbazin/eco-eco-app.git main:gh-pages

cd -