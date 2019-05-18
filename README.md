# A simple Vue + Flask server

## Environments
- CLI: _node.js_ `10.15.3 LTS`
    - PackageManager: _yarn_ `1.15.2`
    - TaskRunner: _Gulp_ `4.0.2`
- Server:
    - _python_ `3.6.7`
    - _Flask_ `1.0.2`

***

### Installation of nodejs modules
```bash
$ yarn add -D gulp browser-sync npm-run-all
```

### Setting up `gulpfile.js`
```javascript
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
```


### Setting up `package.json`
Settings for executing two tasks parallelly.
- `gulp` task (for Auto refreshing the browser: `browser-sync` task)
- `python server.py` task (for Flask webserver task)

Add `scripts` setting to `package.json`.
```json
{
    ...
    "scripts": {
        "server": "python server.py",
        "sync": "gulp",
        "dev": "npm-run-all --parallel server sync"
    }
}
```

***

## How to execute
```bash
$ yarn dev
# => Flask server will run in localhost:8000
# => Gulp task will run: Browser-sync
```
