// Import Webpack npm module
const webpack = require('webpack')
const path = require('path')

module.exports = {
  // Which file is the entry point to the application
  entry: './src/index.jsx',
  // Which file types are in our project, and where they are located
  resolve: {
    extensions: ['.js', '.jsx']
  },
  // Where to output the final bundled code to
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static/dist'),
    sourceMapFilename: 'bundle.map.js'
  },
  devtool: '#source-map',
  devServer: {
      inline: true,
      port: 3000
   },

  module: {
      // How to process project files with loaders
      loaders: [
        // Process any .js or .jsx file with Babel
        {
          test: /\.jsx?$/,
          exclude: /node_modules/,
          loaders: ['babel-loader']
        },
        {
          test: /\.css$/,
          loader: 'style-loader!css-loader'
        },
        {
          test: /\.(PNG|jpg|gif)$/,
          loader: 'file-loader',
          options: {}
        },
        {
          test: /\.(gif|PNG|jpe?g|svg)$/i,
          loader: 'image-webpack-loader',
          options: {}
      },
      {
        test: /\.(PNG|jpg|gif|svg|eot|ttf|woff|woff2)$/,
        loader: 'url-loader',
        options: {}
      }
    ]
  }
}
