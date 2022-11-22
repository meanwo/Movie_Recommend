<template>
  <div id="app">
    <nav class="navbar bg-light home-nav">

      <b-button v-b-toggle.sidebar-backdrop class="moving-nav">Menu</b-button>
      <router-link :to="{ name: 'MainView' }"><img src="@/assets/pat_mat.png" alt="" class="patmat">Pat & Mat TV</router-link>
      <div>
      </div>
      <!-- title="Menu"  -->
      <!-- :backdrop-variant="variant" -->
     
      <b-sidebar 
      id="sidebar-backdrop"
      backdrop
      shadow>
      <router-link :to="{ name: 'MainView' }" class="text-line h3">Main</router-link><p></p>
      <div class="px-3 py-2">
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 28 } }" class="text-line">액션</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 12 } }" class="text-line">모험</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 16 } }" class="text-line">애니메이션</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 35 } }" class="text-line">코미디</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 80 } }" class="text-line">범죄</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 99 } }" class="text-line">다큐멘터리</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 18 } }" class="text-line">드라마</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 10751 } }" class="text-line">가족</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 14 } }" class="text-line">판타지</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 36 } }" class="text-line">역사</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 27 } }" class="text-line">공포</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 10402 } }" class="text-line">음악</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 9648 } }" class="text-line">미스터리</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 10749 } }" class="text-line">로맨스</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 878 } }" class="text-line">SF</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 10770 } }" class="text-line">TV 영화</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 53 } }" class="text-line">스릴러</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 10752 } }" class="text-line">전쟁</router-link></p>
        <p><router-link :to="{ name: 'GenreDetailView', params: { id: 37 } }" class="text-line">서부</router-link></p>
        
      </div>
      </b-sidebar>
     
      <div class="justify-content-flex-end">
        <!-- <router-link v-if="!this.$store.state.token" :to="{ name: 'SignUpView' }">  SignUpPage</router-link> | -->
        <router-link v-if="!this.$store.state.token" :to="{ name: 'LogInView' }">  LogInPage</router-link>
        <router-link v-if="this.$store.state.token" :to="{ name: 'ArticleView' }">  Articles</router-link> |
        <button v-if="this.$store.state.token" class="logoutButton" @click="logOut">Logout</button>
      </div>
    </nav>
    <router-view/>
  </div>
  <!-- <p>navbar navbar-expand-lg bg-light justify-content-center</p> -->
</template>
<script scoped>
export default {
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
    }
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
  /* width: 60px; */
  /* align-items: center; */
  /* justify-content: center; */
  height: 30px;
  position: sticky;
  top: 0;
  /* padding: 0px 0px 3px 0px; */
}
.home-nav{
  /* position:sticky; */
}
.patmat{
  width: 35px;
  height: 35px;
  margin-left: 360px
}
</style>
