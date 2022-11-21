<template>
<<<<<<< HEAD
<div class="card" style="width: 18rem margin-left: 20px; margin-bottom: 20px" @click="goToDetail">
    <img :src="base_url+GenreMovie.poster_path" alt="영화이미지">
    <h4 class="card-title font-weight-bold: 700">{{ GenreMovie.title }}</h4>
</div>  




=======
<div class="col-3 m-3" style="width: 18rem margin-left: 20px; margin-bottom: 20px" @click="goToDetail">
    <img :src="base_url+GenreMovie.poster_path" alt="영화이미지">
    <h4 class="card-title font-weight-bold: 700">{{ GenreMovie.title }}</h4>

  </div>
>>>>>>> c718f2e78a17277d28f1b63038b27e9146baf9bd
</template>

<script>
export default {
    name: 'GenreMovieItem',
    data () {
        const base_url = 'https://image.tmdb.org/t/p/original/'
        return {
          base_url
        }
      },
<<<<<<< HEAD
    
=======
>>>>>>> c718f2e78a17277d28f1b63038b27e9146baf9bd
    props: {
    GenreMovie: Object,
    },
    methods: {
        goToDetail() {
          this.$router.push({ name: 'MovieDetailView', params: {id: this.GenreMovie.id }})
        }
    },
}
</script>

<style>

</style>