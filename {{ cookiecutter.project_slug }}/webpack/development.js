const { WebpackPluginServe: Serve } = require('webpack-plugin-serve')
const fs = require('fs')

module.exports = (config) => {
  const serveOptions = {
    static: config.output.path,
    client: {
      address: (process.env.WEBPACK_HOST || 'localhost') + ':55555'
    },
    middleware: (app) =>
      app.use(async (ctx, next) => {
        await next()
        ctx.set('Access-Control-Allow-Origin', '*')
      })
  }

  if (process.env.SSL_KEY && process.env.SSL_CERT) {
    serveOptions.https = {
      key: fs.readFileSync(process.env.SSL_KEY),
      cert: fs.readFileSync(process.env.SSL_CERT)
    }
  }

  config.entry.main.push('webpack-plugin-serve/client')
  config.output.publicPath = 'http' + (serveOptions.https ? 's' : '') + '://' + serveOptions.client.address + '/'
  config.plugins.push(new Serve(serveOptions))
}
