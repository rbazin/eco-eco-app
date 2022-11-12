// To correctly export the frontend on github pages

module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/eco-eco-app/'
    : '/'

}
