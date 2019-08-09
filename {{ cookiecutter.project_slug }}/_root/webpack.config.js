const path = require('path')

const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const EventHooksPlugin = require('event-hooks-webpack-plugin')
const BundleTracker = require('webpack-bundle-tracker')

const nucleusConfigGenerator = require('./{{ cookiecutter.project_slug }}/webpack/nucleus.js')
const developmentConfig = require('./{{ cookiecutter.project_slug }}/webpack/development.js')
const productionConfig = require('./{{ cookiecutter.project_slug }}/webpack/production.js')

const buildPath = path.resolve(__dirname, '{{ cookiecutter.project_slug }}', 'webpack', 'dist')

module.exports = (env, argv) => {
  const development = argv.mode === 'development'

  const config = {
    devtool: 'source-map',
    entry: {
      main: [ './{{ cookiecutter.project_slug }}/webpack/src/index.js' ]
    },
    output: {
      filename: development ? '[name].js' : '[name].[hash:20].js',
      path: buildPath
    },
    node: {
      fs: 'empty'
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        },
        {
          test: /\.(s?css)$/,
          use: [
            development ? {
              // creates style nodes from JS strings
              loader: 'style-loader'
            } : {
              loader: MiniCssExtractPlugin.loader
            },
            {
              // translates CSS into CommonJS
              loader: 'css-loader',
              options: {
                sourceMap: true
              }
            },
            {
              // Runs compiled CSS through postcss for vendor prefixing
              loader: 'postcss-loader',
              options: {
                sourceMap: true
              }
            },
            {
              // compiles Sass to CSS
              loader: 'sass-loader',
              options: {
                outputStyle: 'expanded',
                sourceMap: true
              }
            }
          ]
        },
        {
          // Load all images as base64 encoding if they are smaller than 8192 bytes
          test: /\.(png|jpg|gif)$/,
          use: [
            {
              loader: 'url-loader',
              options: {
                name: development ? '[path][name].[ext]' : '[name].[hash:20].[ext]',
                limit: 1
              }
            }
          ]
        },
        {
          test: /\.(woff2?|ttf|otf|eot|svg)$/,
          use: [
            {
              loader: 'file-loader',
              options: {
                name: development ? '[path][name].[ext]' : '[name].[hash:20].[ext]'
              }
            }
          ]
        }
      ]
    },
    plugins: [
      new EventHooksPlugin({
        done: nucleusConfigGenerator
      }),
      new CleanWebpackPlugin(),
      new BundleTracker({
        filename: './webpack-stats.json'
      })
    ],
    watchOptions: {
      poll: true
    }
  }

  development ? developmentConfig(config) : productionConfig(config)

  return config
}
