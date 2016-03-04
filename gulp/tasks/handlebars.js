/**
 * Dependencies
 */
const fs = require('fs');
const gulp  = require('gulp');
const handlebars = require('gulp-compile-handlebars');
const path = require('path');
const rename = require('gulp-rename');

/**
 * Module body / Expose
 */
module.exports = function(manifestPath, scriptSourceTemplate, staticRoot) {
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const handlebarOpts = {
            helpers: {
                assetPath: function(path, context) {
                    return [staticRoot, context.data.root[path]].join('/');
                }
            }
        };
  const outputFile = path.basename(scriptSourceTemplate).replace('.hbs', '.html');
  return gulp.src(scriptSourceTemplate)
      .pipe(handlebars(manifest, handlebarOpts))
      .pipe(rename(outputFile));
};
