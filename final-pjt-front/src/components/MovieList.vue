<template>
    <div class="card enlarge" style="width: 18rem margin-left: 20px; margin-bottom: 20px" @click="goToDetail">
      <!-- <router-link :to="{name: 'MovieDetailView', params: {id: movieCard.id }}"> -->
        <img :src="base_url+movieCard.poster_path" alt="영화이미지">
      <!-- </router-link> -->
      <!-- <img :src="base_url+movieCard.poster_path" alt="영화이미지"> -->
      <!-- <h5 class="card-title font-weight-bold: 700">{{ movieCard.original_title }}</h5> -->
      <h4 class="card-title font-weight-bold: 700">{{ movieCard.title }}</h4>
      <!-- {{ movieCard.id }} -->
      {{ movieCard }}

    </div>
  </template>
  
  <script>
  export default {
      name: 'MovieList',
      data () {
        const base_url = 'https://image.tmdb.org/t/p/original/'
        return {
          base_url
        }
      },
      props: {
        movieCard: {
          type: Object,
        },
      },
      methods: {
        goToDetail() {
          this.$router.push({ name: 'MovieDetailView', params: {id: this.movieCard.id }})
        }
      }
      // computed: {
      //   printMovieCard() {
      //     console.log(this.movieCard)
      //     return this.movieCard
      //   }
      // }
  }
  </script>
  
  <style>
    .enlarge:hover img{
      transform: scale(1.5,1.5);
    }
  </style>