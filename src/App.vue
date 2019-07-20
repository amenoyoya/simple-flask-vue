<template>
  <v-app>
    <v-content>
      <v-container>
        <v-layout wrap>
          <v-flex xs12 sm6 md4>
            コンテンツ
          </v-flex>
          <v-flex xs12 sm6 md4>
            <v-alert :value="true" type="success">{{ message }}</v-alert>
          </v-flex>
          <v-flex xs12 sm6 md4>
            コンテンツ
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  data(){
    return {
      message: ''
    }
  },
  async created(){
    const res = await axios.get('http://localhost:8000/api/');
    console.log(res);
    if (res.status === 200) {
      this.message = res.data.message;
    }
  }
}
</script>