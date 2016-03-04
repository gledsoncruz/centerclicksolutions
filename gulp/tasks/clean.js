/**
 * Dependencies
 */
const del = require('del');

/**
 * Module body / Expose
 */
module.exports = function(entry, config) {
  config = config || {};
  return del(entry, config);
};
