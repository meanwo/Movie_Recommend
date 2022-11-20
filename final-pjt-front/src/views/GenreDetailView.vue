<template>
  <div>
    
    <GenreMovieItem
      v-for="GenreMovie in GenreMovies"
      :key="GenreMovie.id"
      :GenreMovie="GenreMovie"
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