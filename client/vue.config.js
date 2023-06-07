const path = require('path');

module.exports = {
  transpileDependencies: true,
  chainWebpack: (config) => {
    config.module
        .rule('fonts')
        .test(/\.(ttf|otf|eot|woff|woff2)$/)
        .use('file-loader')
        .loader('file-loader')
        .tap((options) => {
          options.name = 'fonts/[name].[hash:8].[ext]';
          return options;
        });
  },
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'),
      },
    },
  },
};