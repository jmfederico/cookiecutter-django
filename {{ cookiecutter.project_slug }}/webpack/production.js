const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin')

module.exports = (config) => {
  config.plugins.push(...[
    new MiniCssExtractPlugin({
      filename: 'styles.[hash:20].css'
    }),
    new OptimizeCssAssetsPlugin({
      cssProcessor: require('cssnano'),
      cssProcessorOptions: {
        map: {
          inline: false
        },
        discardComments: {
          removeAll: true
        }
      },
      canPrint: true
    })
  ])
}
