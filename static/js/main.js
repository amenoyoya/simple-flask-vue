var app = new Vue({
    el: '#app',
    data: {
        title: '',
        content: ''
    },
});

// APIサーバーを叩く
axios.get('/api/')
.then(function(res) {
    app.title = res.data.admin.title;
    app.content = res.data.admin.content;
})
.catch(function(err) {
    console.log(err);
});
