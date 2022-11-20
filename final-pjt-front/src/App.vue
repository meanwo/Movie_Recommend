<template>
  <div id="app">
    <nav class="navbar bg-light">
      <b-button v-b-toggle.sidebar-backdrop>Menu</b-button>
      <div>
      </div>
      <!-- title="Menu"  -->
      <!-- :backdrop-variant="variant" -->
      <b-sidebar 
      id="sidebar-backdrop" 
      backdrop
      shadow>
      <router-link :to="{ name: 'MainView' }">Main</router-link>
      <div class="px-3 py-2">
        <p>액션</p>
        <p>스릴러</p>
        <p>드라마</p>
        <p>공포</p>
      </div>
      </b-sidebar>
      <div class="justify-content-flex-end">
        <router-link v-if="!this.$store.state.token" :to="{ name: 'SignUpView' }">  SignUpPage</router-link> |
        <router-link v-if="!this.$store.state.token" :to="{ name: 'LogInView' }">  LogInPage</router-link>
        <router-link v-if="this.$store.state.token" :to="{ name: 'ArticleView' }">  Articles</router-link> |
        <button v-if="this.$store.state.token" class="logoutButton" @click="logOut">Logout</button>
      </div>
    </nav>
    <router-view/>
  </div>
  <!-- <p>navbar navbar-expand-lg bg-light justify-content-center</p> -->
</template>
<script>
export default {
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* position: static;
  z-index: 2; */
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
