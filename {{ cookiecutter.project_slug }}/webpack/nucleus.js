const fs = require('fs')

module.exports = (stats) => {
  if (stats.compilation.errors.length > 0) {
    return
  }

  const nucleus = {
    'title': 'Nucleus',
    'files': [
      '{{ cookiecutter.project_slug }}/webpack/src/**/*.scss'
    ],
    'target': '{{ cookiecutter.project_slug }}/styleguide/dist/styleguide',
    'namespace': 'page',
    'verbose': 3,
    'counterCSS': null,
    'staticLipsum': false,
    'placeholderService': false,
    'css': [],
    'scripts': []
  }

  stats.compilation.chunks.forEach(chunk => {
    const basePath = '/static/'
    chunk.files.forEach(file => {
      if (file.endsWith('.js')) {
        nucleus.scripts.push(basePath + file)
        return
      }

      if (file.endsWith('.css')) {
        nucleus.css.push(basePath + file)
      }
    })
  })

  fs.writeFileSync(
    'config.nucleus.json',
    JSON.stringify(nucleus, null, 2)
  )
}
