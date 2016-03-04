/**
 * Dependencies
 */
const cleanup = require('gulp-cleanup');

/**
 * Module body / Expose
 */
module.exports = function(config) {
  config = config || {};
  return cleanup();
};
