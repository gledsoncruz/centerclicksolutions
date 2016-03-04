/**
 * Dependencies
 */
const gulp = require('gulp');

/**
 * Module body
 */
module.exports = function(entry, config) {
  config = config || {};
  return gulp.src(entry, config);
};
