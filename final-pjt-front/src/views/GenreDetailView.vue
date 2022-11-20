<template>
<div class="row d-flex justify-content-center p-3 mb-2 bg-dark">
<h1 class="text-light p-3"> {{this.$route.params.genreName}}</h1>

  <GenreMovieItem
    v-for="GenreMovie in GenreMovies"
    :key="GenreMovie.id"
    :GenreMovie="GenreMovie"
    class="col-3 m-3"
  />
  </div>


</template>

<script>
import GenreMovieItem from '@/components/GenreMovieItem'
export default {
    name: 'GenreDetailView',
    components: {
      GenreMovieItem
    },
    data() {
        return {
            genreMovie: null,
        }
    },
    created() {
       window.scrollTo( { top: 0, behavior: "smooth"})
    },
    computed: {
      GenreMovies() {
        let GenreMovieList = [];
        for(let i = 0; i <this.$store.state.totalMovies.length; i++){
          for(let j = 0; j <this.$store.state.totalMovies[i].genres.length; j++){
            
            if (this.$store.state.totalMovies[i].genres[j].id == this.$route.params.id) {
              GenreMovieList.push(this.$store.state.totalMovies[i])
              break;
            }
          }
        }
        return GenreMovieList
      }
      }
    }

  

</script>

<style>

</style>