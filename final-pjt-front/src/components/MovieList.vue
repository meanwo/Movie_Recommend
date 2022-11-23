<template>
    <div class="card-group enlarge mb-5" style="width: 18rem; margin-left: 20px; margin-bottom: 20px" @click="goToDetail">
      <!-- <router-link :to="{name: 'MovieDetailView', params: {id: movieCard.id }}"> -->
        <img  class="card-img-top img-card" :src="base_url+movieCard.poster_path" alt="영화이미지">
      <!-- </router-link> -->
      <!-- <img :src="base_url+movieCard.poster_path" alt="영화이미지"> -->
      <!-- <h5 class="card-title font-weight-bold: 700">{{ movieCard.original_title }}</h5> -->
      <div class="card-title">
        <h5 class=" font-weight-bold: 700 movie-list-page each-card-text text-light">{{ movieCard.title }}</h5>
      </div>
      
      <!-- {{ movieCard.id }} -->
      <!-- {{ movieCard }} -->

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
          console.log()
          this.$router.push({ name: 'MovieDetailView', params: {id: this.movieCard.id } })
        }
      },
       // computed: {
       //  printMovieCard() {
       //    console.log(this.movieCard)
       //    return this.movieCard
       // }
       // }
  }
  </script>
  
  <style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&display=swap');
    .enlarge:hover img{
      transform: scale(1.1,1.1);
    }
    .movie-list-page {
      display: block;
      text-align: center;
      font-family: 'Noto Sans KR', sans-serif
      text-light
    }
    
    .img-card{
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: 0;
      image-rendering: pixelated;
      image-rendering: -webkit-optimize-contrast;
      transform: translateZ(0);
      backface-visibility: hidden;

    }
    .each-card-text{
      z-index: 1;
      /* display:flex; */
      /* text-align: center; */
    }
    .card-title{
      display: flex;
      text-align: center;
      word-break: keep-all;   
    }
  </style>