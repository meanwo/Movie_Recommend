<template>
  <div>
    {{GenreMovies}}
    {{$route.params.id}}
    <!-- {{ $store.state.totalMovies[0].genres}} -->
    {{ $store.state.totalMovies[0]}}
  </div>
</template>

<script>
// import axios from 'axios';
export default {
    name: 'GenreDetailView',
   
    data() {
        return {
            genreMovie: null,
        }
    },
    computed: {
      GenreMovies() {
        let GenreMovieList = [];
        function getKeyByValue(obj, value) {
          return Object.keys(obj).find(key => obj[key] === value);
        }
        for(let i = 0; i <this.$store.state.totalMovies.length; i++){
          for(let j = 0; j<this.$store.state.totalMovies[i].genres.length; j++){
            if (getKeyByValue(this.$store.state.totalMovies[i].genres, this.$route.params.id) !== undefined){
              GenreMovieList.push(this.$store.state.totalMovies[i])

            }
          }
        }
        return GenreMovieList
      }
      // const genreMovies = this.$store.state.totalMovies.filter(movie => movie.genres.id == this.$route.params.id) {
      //   return this.$store.state.totalMovies
      }
    }

  

</script>

<style>

</style>