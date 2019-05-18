var app = new Vue({
    el: '#app',
    data: {
        title: '',
        content: ''
    },
});

axios.get('/static/data/users.json')
.then(function(res) {
    app.title = res.data.admin.title;
    app.content = res.data.admin.content;
})
.catch(function(err) {
    console.log(err);
});
