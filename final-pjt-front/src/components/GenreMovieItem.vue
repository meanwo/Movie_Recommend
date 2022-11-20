<template>
<div class="col-3 m-3" style="width: 18rem margin-left: 20px; margin-bottom: 20px" @click="goToDetail">
    <img :src="base_url+GenreMovie.poster_path" alt="영화이미지">
    <h4 class="card-title font-weight-bold: 700">{{ GenreMovie.title }}</h4>

  </div>
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