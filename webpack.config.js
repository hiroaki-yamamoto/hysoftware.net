const {AngularCompilerPlugin} = require('@ngtools/webpack/src');

module.exports = (config) => {
  config.module.rules.unshift(
    {
      test: /.(pug|jade)$/,
      exclude: /.(include|partial).(pug|jade)$/,
      use: [{ loader: 'apply-loader' }, { loader: 'pug-loader' }]
    },
    { test: /.(include|partial).(pug|jade)$/, loader: 'pug-loader' }
  );

  const index = config.plugins.findIndex(
    p => {
      return p instanceof AngularCompilerPlugin
    },
  );
  const oldOptions = config.plugins[index].options;
  oldOptions.directTemplateLoading = false;
  config.plugins.splice(index);

  config.plugins.push(
    new AngularCompilerPlugin(oldOptions)
  );

  return config;
};
