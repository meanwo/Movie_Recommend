<template>
  <div
    class="card recommend-movies enlarge"
    style="width: 18rem margin-left: 20px; margin-bottom: 20px"
    @click="goToDetail"
  >
    <img :src="base_url + RecommendMovie.poster_path" alt="영화이미지" />
    <h4 class="card-title font-weight-bold: 700">{{ RecommendMovie.title }}</h4>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "RecommendListItem",
  data() {
    const base_url = "https://image.tmdb.org/t/p/original/";
    return {
      base_url,
      RecommendMovie: "",
    };
  },
  created() {
    this.getRecommendMovie();
  },
  props: {
    RecommendPk: Number,
  },
  methods: {
    getRecommendMovie() {
      axios({
        method: "get",
        url: `${API_URL}/api/v2/movies/${this.RecommendPk}`,
      })
        .then((res) => {
          this.RecommendMovie = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goToDetail() {
      location.href = `http://localhost:8080/movies/${this.RecommendPk}`;
    },
  },
};
</script>

<style scoped>
.recommend-movies {
  zoom: 90%;
}
.enlarge:hover img{
  transform: scale(1.1,1.1);
}
</style>
