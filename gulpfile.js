const gulp = require('gulp');
const exec = require('child_process').exec;

// `webserver` task: Flask server
gulp.task('webserver', function(done) {
    // Flask will run in localhost:8000
    exec('python server.py', function(err, stdout, stderr) {
        console.log(stdout);
        console.error(stderr);
    });
    // This task will be running forever, not be finished
    // done();
});

// `default` task: gulp command will execute this task
//   => execute `webserver` task
//   if you want to execute multiple tasks: use gulp.series('task1', 'task2', ...)
//   if you want to execute parallel tasks: use gulp.parallel('task1', 'task2', ...)
gulp.task('default', gulp.task('webserver'));
