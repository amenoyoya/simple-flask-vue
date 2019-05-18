var gulp          = require("gulp");
var browserSync   = require('browser-sync').create();
var reload        = browserSync.reload;

// `browser-sync` task: Refresh the browser Automatically
gulp.task('browser-sync', function(done) {
    browserSync.init({
        // Set target host for refreshing: localhost:8000(Flask Server)
        proxy: "localhost:8000"
    });
    // This task will be running forever, not be finished
    // done();
});

// `watch` task: Watch changing of files, and reload browser-sync
gulp.task("watch", function (done) {
    gulp.watch(['./html/**/*']).on("change", reload);
    // This task will be running forever, not be finished
    // done();
});

// `default` task: gulp command will execute this task
//   => execute `browser-sync` and `watch` tasks parallelly
//   if you want to execute one task: use gulp.task('task')
//   if you want to execute multiple tasks serially: use gulp.series('task1', 'task2', ...)
gulp.task("default", gulp.parallel("browser-sync", "watch"));
