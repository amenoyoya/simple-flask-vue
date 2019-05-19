var app = new Vue({
    el: '#app',
    data: {
        users: [],
        user: '',
        title: '',
        content: ''
    },
    methods: {
        switch_user(user){
            // APIサーバーを叩いて、ユーザー情報を取得
            axios.get('/api/users')
            .then(function(res) {
                app.users = Object.keys(res.data);
                data = res.data[user];
                if (data) {
                    app.user = user;
                    app.title = data.title;
                    app.content = data.content;
                }
            })
            .catch(function(err) {
                console.log(err);
            });
        }
    }
});

app.switch_user('admin');
