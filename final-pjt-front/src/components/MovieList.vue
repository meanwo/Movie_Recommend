<template>
  <div class="card-group enlarge mb-5" style="width: 18rem" @click="goToDetail">
    <img
      class="card-img-top img-card"
      :src="base_url + movieCard.poster_path"
      alt="영화이미지"
    />
    <div class="card-title">
      <h5
        class="font-weight-bold: 700 movie-list-page each-card-text text-light mt-2"
      >
        {{ movieCard.title }}
      </h5>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieList",
  data() {
    const base_url = "https://image.tmdb.org/t/p/original/";
    return {
      base_url,
    };
  },
  props: {
    movieCard: {
      type: Object,
    },
  },
  methods: {
    goToDetail() {
      this.$router.push({
        name: "MovieDetailView",
        params: { id: this.movieCard.id },
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
  display: block;
  text-align: center;
  font-family: "Noto Sans KR", sans-serif text-light;
}

.img-card {
  object-fit: cover;
  z-index: 0;
  image-rendering: -webkit-optimize-contrast;
  transform: translateZ(0);
  backface-visibility: hidden;
}
.each-card-text {
  z-index: 1;
  display: flex;
  justify-content: center;
  text-align: center;
}
.card-title {
  display: flex;
  word-break: keep-all;
}
</style>
