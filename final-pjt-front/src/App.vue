<template>
  <div id="app">
    <nav class="navbar bg-light">
      <b-button v-b-toggle.sidebar-backdrop class="moving-nav">≡</b-button>
      <!-- <MainView :/> -->
      <button @click="goToMain" class="text-line h3"><img src="@/assets/logo.png" alt="" class="patmat">Pat & Mat TV</button>


      <div>
      </div>
      <!-- title="Menu"  -->
      <!-- :backdrop-variant="variant" -->
     
      <b-sidebar 
      
      id="sidebar-backdrop"
      backdrop
      shadow>
      <!-- <router-link :to="{ name: 'MainView' }" class="text-line h3">Main</router-link> -->
      <button @click="goToMain" class="text-line h3">Main</button>
      <div class="px-3 py-2">
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 28 } }" class="text-line">액션</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 14 } }" class="text-line">판타지</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 18 } }" class="text-line">드라마</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 27 } }" class="text-line">공포</router-link></p>
        
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
  // import MainView from '@/views/Mainview'

export default {
  name: 'App',
  // components: {
  //   MainView
  // },
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
    },
    goToMain() {
      this.$store.dispatch('loadMovieCards', 1)
    },
  }
}
</script>
<style>
#app { /* 라우터 사이 | 색깔*/
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

nav a { /* navbar 라우터 글씨 색*/
  font-weight: bold;
  color:#2c3e50;
}

nav a.router-link-exact-active {
  /* color: #42b983; */
  color:black;
}
.text-line {
  text-decoration-line: none;
}
.moving-nav{
  height: 30px;
  position: sticky;
  top: 0;
}
</style>
