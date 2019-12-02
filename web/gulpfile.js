/*=============================================>>>>>
= Dependencies =
===============================================>>>>>*/
var gulp = require('gulp'),
  uglify = require('gulp-uglify'),
  concat = require('gulp-concat'),
  concatCSS = require('gulp-concat-css'),
  cleanCSS = require('gulp-clean-css'),
  sass = require('gulp-ruby-sass'),
  imagemin = require('gulp-imagemin'),
  plumber = require('gulp-plumber'),
  browserSync = require('browser-sync'),
  reload = browserSync.reload;
/*= End of Dependencis =*/
/*=============================================<<<<<*/


/*=============================================>>>>>
= Paths =
===============================================>>>>>*/

var srcPath = {
  jsPath: 'js/',
  sassPath: 'css/scss/',
  cssPlugins: 'css/plugins/',
  jsPlugins: 'js/plugins/',
  imgPath: 'img/'
};
var destPath = {
  cssPath: 'css/',
  cssPlugins: 'css/plugins/',
  jsPlugins: 'js/plugins/',
  imgPath: 'img/'
};

/*= End of Paths =*/
/*=============================================<<<<<*/


/*=============================================>>>>>
= Gulp Tasks =
===============================================>>>>>*/

/*----------- Styles - Compiles SCSS  -----------*/
gulp.task('styles', function() {
  return sass(srcPath.sassPath + '**/*.scss', {
      style: 'compressed'
    })
    .pipe(plumber())
    .pipe(gulp.dest(destPath.cssPath))
    .pipe(reload({
      stream: true
    }));
});

/*----------- Imagemin - Compresses images -----------*/
gulp.task('imageMin', function() {
  gulp.src(srcPath.imgPath + '*.*')
    .pipe(imagemin(
      [
        imagemin.gifsicle({
          interlaced: true
        }),
        imagemin.jpegtran({
          progressive: true
        }),
        imagemin.optipng({
          optimizationLevel: 5
        }),
        imagemin.svgo({
          plugins: [{
            removeViewBox: true
          }]
        })
      ]
    ))
    .pipe(gulp.dest(destPath.imgPath));
});

/*----------- Plugins Styles - Concatenates Plugins CSS files -----------*/
gulp.task('pluginStyles', function() {
  gulp.src(srcPath.cssPlugins + '*.css')
    .pipe(plumber())
    .pipe(concatCSS("plugins.min.css"))
    .pipe(cleanCSS())
    .pipe(gulp.dest(destPath.cssPlugins));
});

/*----------- Plugins Scritps - Concatenates Plugins JS files -----------*/
gulp.task('pluginScripts', function() {
  gulp.src(srcPath.jsPlugins + '*.js')
    .pipe(plumber())
    .pipe(concat("plugins.min.js"))
    .pipe(uglify())
    .pipe(gulp.dest(destPath.jsPlugins));
});

/*----------- HTML - Watches for Changes in HTML for BrowserSync  -----------*/
gulp.task('html', function() {
  gulp.src('**/*.html')
    .pipe(reload({
      stream: true
    }));
});

/*----------- Scripts - Watches for Changes in main.js for BrowserSync  -----------*/
gulp.task('scripts', function() {
  gulp.src(srcPath.jsPath + 'main.js')
    .pipe(reload({
      stream: true
    }));
});

/*----------- BrowserSync Task -----------*/
gulp.task('browser-sync', function() {
  browserSync.init({
    server: {
      baseDir: "./"
    }
  });
});

/*----------- Watch task - Watches files for changes -----------*/
gulp.task('watch', function() {
  gulp.watch(srcPath.sassPath + '**/*.scss', ['styles']);
  gulp.watch('**/*.html', ['html']);
  gulp.watch(srcPath.jsPath + '**/*.js', ['scripts']);
});

/*----------- Default Task -----------*/
gulp.task('default', ['styles', 'html', 'scripts', 'browser-sync', 'watch']);
/*= End of Gulp Tasks =*/
/*=============================================<<<<<*/