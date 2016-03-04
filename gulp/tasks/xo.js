/**
 * Dependencies
 */
const gulp = require('gulp');
const xo   = require('gulp-xo');

/**
 * Module body / Expose
 */
module.exports = function(entry, config) {
  config = config || {};
  return gulp.src(entry)
    .pipe(xo());
};
