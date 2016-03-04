/**
 * Dependencies
 */
const gulp  = require('gulp');
const mocha = require('gulp-mocha');

/**
 * Module body / Expose
 */
module.exports = function(entry, config) {
  config = config || {};
  return gulp.src(entry, config)
    .pipe(mocha({
      require: [
        'babel-register'
      ]
    }));
};
