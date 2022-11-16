<template>
  <div class="row d-flex justify-content-center">
    <h1>Main</h1>
    <MovieList/>
    
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
    name: 'MovieView',
    components: {
        MovieCard,
    },
    created: function() {
        this.$store.dispatch('loadMovieCards')
    },
    computed: {
        movieCards() {
            // console.log(this.$store.state.movieCards)
            return this.$store.state.movieCards
        },
    // methods: {
    //     changePage() {
    //         this.$store.dispatch('loadMovieCards')
    //     }
    // }
        
            
    }

    
}
</script>

<style>

</style>