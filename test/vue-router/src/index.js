import Vue from 'vue';
import App from './App';
import Footer from './Footer';
import Vuetify from 'vuetify';
import Router from 'vue-router';
// vuetifyのスタイルシートload
import 'vuetify/dist/vuetify.min.css';
// icons
import 'material-design-icons-iconfont/dist/material-design-icons.css';
import '@fortawesome/fontawesome-free/css/all.css';
// IE11/Safari9用のpolyfill
import 'babel-polyfill';

import About from './About';
import Dashboard from './Dashboard';

Vue.use(Vuetify); // Vuetifyのコンポーネントを使用可能に
// フッターコンポーネント登録
Vue.component('my-footer', Footer);

// ルーター設定
Vue.use(Router);
const router = new Router({
  mode: 'history',
  routes: [
    {path: '/about', component: About},
    {path: '/dashboard', component: Dashboard},
  ]
});

new Vue({
  el: "#app",
  router,
  components: { App },
  template: '<App/>'
});