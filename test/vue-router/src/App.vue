<template>
  <v-app>
    <v-content>
      <v-card>
        <v-card-title><h1>Links</h1></v-card-title>
        <v-card-text>
          <ul>
            <li><router-link to="/about">About</router-link></li>
            <li><router-link to="/dashboard">Dashboard</router-link></li>
          </ul>
        </v-card-text>
      </v-card>
      <router-view></router-view>
    </v-content>
    <my-footer></my-footer>
  </v-app>
</template>