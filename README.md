# A simple Vue + Flask server

## Environments
- CLI: _node.js_ `10.15.3 LTS`
    - PackageManager: _yarn_ `1.15.2`
    - TaskRunner: _Gulp_ `4.0.2`
- Server:
    - _python_ `3.6.7`
    - _Flask_ `1.0.2`

***

### Installation of Gulp
```bash
$ yarn add -D gulp
```

#### Setting of gulpfile.js
```javascript
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
```

***

## How to execute
```bash
$ yarn gulp
# => Flask server will run in localhost:8000
```
