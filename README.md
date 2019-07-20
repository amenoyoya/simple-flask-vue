# A simple Vue + Flask server

## What's this
- A simple web application template
    - Backend: Python + Flask Server
    - Frontend: Vue + Vuetify

***

## Introduction

### Environments
- Terminal: _Bash_
    - If in Windows, use `Git Bash for Windows`
- CLI: _node.js_ `10.15.3 LTS`
    - PackageManager: _yarn_ `1.15.2`
    - DownloadManager: _curl_
- Server:
    - _python_ `3.6.7`
    - _Flask_ `1.0.2`

---

### Setup

#### Create Vuetify Project
```bash
# create minimal vuetify project
$ curl https://raw.githubusercontent.com/amenoyoya/node-projects/master/vuetify.js | node -

# install node modules
$ yarn install

# run webpack-dev-server
$ yarn start

# => Run Vuetify App on http://localhost:3000
```

- Minimal Vuetify Project:
    ```conf
    ./
    |- public/
    |   `- index.html
    |- src/
    |   |- App.vue
    |   `- index.js
    |- package.json
    |- tsconfig.json
    `- webpack.config.js
    ```
