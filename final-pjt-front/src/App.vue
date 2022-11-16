<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-light justify-content-center">
      <router-link :to="{ name: 'MainView' }"> Main</router-link> |
      <router-link v-if="this.$store.state.token" :to="{ name: 'ArticleView' }">  Articles</router-link> |
      <router-link v-if="!this.$store.state.token" :to="{ name: 'SignUpView' }">  SignUpPage</router-link> |
      <router-link v-if="!this.$store.state.token" :to="{ name: 'LogInView' }">  LogInPage</router-link>
      <button v-if="this.$store.state.token" class="logoutButton" @click="logOut">Logout</button>
    </nav>
    <router-view/>
  </div>
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
