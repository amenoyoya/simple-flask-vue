var gulp          = require("gulp");
var browserSync   = require('browser-sync').create();
var reload        = browserSync.reload;
var exec          = require('child_process').exec;

var source        = "./html/**/*"

gulp.task('browser-sync', function() {
  browserSync.init({
    //変更
    proxy: "localhost:8000"
  });
});

gulp.task("watch", function () {
    gulp.watch([source]).on("change", reload);
});
/*
gulp.task('server', function() {
    exec('python server.py');
});
*/
gulp.task("default", gulp.parallel(/*'server',*/ "browser-sync", "watch"));
