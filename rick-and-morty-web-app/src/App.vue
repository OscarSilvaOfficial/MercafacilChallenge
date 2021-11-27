<template>
  <v-app>
    <v-main>
      <!-- <Menu /> -->
      <router-view/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
// import Menu from '@/components/Menu.vue'

export default Vue.extend({
  name: 'App',
  components: {
    // Menu,
  }
});
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Merienda&display=swap');

@font-face {
  font-family: "ReM";
  src: local("ReM"), url(./assets/fonts/get-schwifty.ttf) format("truetype");
}

html {
  overflow: auto !important; 
}

.font-rem {
  font-family: "ReM", Helvetica, Arial;
  font-size: 24px;
  font-weight: 800;
  margin-top: 24px;
  color: black;
}

.list {
  height: 100vh;
  background-color: #fff;
  padding: 30px 90px;
  background-color: #1e1e1e;
}
</style>
