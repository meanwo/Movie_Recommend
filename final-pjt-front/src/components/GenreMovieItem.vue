<template>
  <div
    class="card-group enlarge mb-5"
    style="width: 18rem; margin-left: 20px; margin-bottom: 20px"
    @click="goToDetail"
  >
    <img
      class="card-img-top img-card"
      :src="base_url + GenreMovie.poster_path"
      alt="영화이미지"
    />
    <h4
      class="card-title font-weight-bold: 700 movie-list-page card-title each-card-text text-light"
    >
      {{ GenreMovie.title }}
    </h4>
  </div>
</template>

<script>
export default {
  name: "GenreMovieItem",
  data() {
    const base_url = "https://image.tmdb.org/t/p/original/";
    return {
      base_url,
    };
  },

  props: {
    GenreMovie: Object,
  },
  methods: {
    goToDetail() {
      this.$router.push({
        name: "MovieDetailView",
        params: { id: this.GenreMovie.id },
      });
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&display=swap");

.enlarge:hover img {
  transform: scale(1.1, 1.1);
}
.movie-list-page {
  font-family: "Noto Sans KR", sans-serif text-light;
}
.img-card {
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
  image-rendering: pixelated;
  image-rendering: -webkit-optimize-contrast;
  transform: translateZ(0);
  backface-visibility: hidden;
}
.card-title {
  text-align: center;
}
.each-card-text {
  z-index: 1;
  display: flex;
}
</style>
