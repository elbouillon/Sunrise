var gulp = require('gulp'),
    browserSync = require('browser-sync'),
    process = require('child_process'),
    sass = require('gulp-sass');

var reload = browserSync.reload;
var exec = process.exec;

gulp.task('runserver', function() {
    var proc = exec('python manage.py runserver');
});

gulp.task('styles', function() {
    gulp.src('sunrise_web/static/sass/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('sunrise_web/static/css/'));
});

gulp.task('default', ['runserver'], function() {
    browserSync({
        notify: false,
        proxy: "127.0.0.1:5000/alarm"
    });

    gulp.watch(['sunrise_web/alarm/templates/**'], reload);
    gulp.watch('sunrise_web/static/sass/*.scss', ['styles']);
});