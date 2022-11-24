<template>
  <div
    class="row d-flex justify-content-center text-align-center p-3 mb-2 bg-dark main-page"
  >
    <h1 class="text-light p-3 main-txt">Main</h1>

    <MovieList
      v-for="movieCard in movieCards"
      :key="movieCard.id"
      :movieCard="movieCard"
      class=".col-6 col-md-3 col-lg-1 m-2 mb-3"
    />
    <div class="mt-5 page-button">
      <button @click.self="FirstPage">&lt;&lt;</button>
      <button @click.self="FrontPage">&lt;</button>
      <button @click="ChangePage">{{ n1 }}</button>
      <button @click="ChangePage">{{ n2 }}</button>
      <button @click="ChangePage">{{ n3 }}</button>
      <button @click="ChangePage">{{ n4 }}</button>
      <button @click="ChangePage">{{ n5 }}</button>
      <button @click="ChangePage">{{ n6 }}</button>
      <button @click="ChangePage">{{ n7 }}</button>
      <button @click.self="BackPage">></button>
      <button @click.self="EndPage">>></button>
    </div>
  </div>
</template>

<script>
import MovieList from "@/components/MovieList";

export default {
  name: "MovieView",
  components: {
    MovieList,
  },
  data() {
    return {
      n1: 1,
      n2: 2,
      n3: 3,
      n4: 4,
      n5: 5,
      n6: 6,
      n7: 7,
    };
  },
  created: function () {
    this.$store.dispatch("loadTotalMovies");
  },
  computed: {
    movieCards() {
      return this.$store.state.movieCards;
    },
  },
  methods: {
    ChangePage(event) {
      const num = event.target.innerText;
      this.$store.dispatch("loadMovieCards", num);
      this.$router.push({ name: "MainView", params: { id: num } });
    },
    BackPage() {
      if (this.n7 + 7 < 500) {
        (this.n1 += 7), (this.n2 += 7), (this.n3 += 7), (this.n4 += 7);
        (this.n5 += 7), (this.n6 += 7), (this.n7 += 7);
        this.$store.dispatch("loadMovieCards", this.n1);
      }
      console.log(this.n1, this.n7);
    },
    FrontPage() {
      if (this.n1 - 7 > 0) {
        (this.n1 -= 7), (this.n2 -= 7), (this.n3 -= 7), (this.n4 -= 7);
        (this.n5 -= 7), (this.n6 -= 7), (this.n7 -= 7);
        this.$store.dispatch("loadMovieCards", this.n7);
      }
    },
    FirstPage() {
      (this.n1 = 1), (this.n2 = 2), (this.n3 = 3), (this.n4 = 4);
      (this.n5 = 5), (this.n6 = 6), (this.n7 = 7);
      this.$store.dispatch("loadMovieCards", this.n1);
    },
    EndPage() {
      (this.n1 = 494), (this.n2 = 495), (this.n3 = 496), (this.n4 = 497);
      (this.n5 = 498), (this.n6 = 499), (this.n7 = 500);
      this.$store.dispatch("loadMovieCards", 500);
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&display=swap");
.main-txt {
  font-family: "Noto Sans KR", sans-serif;
}
.main-page {
  zoom: 90%;
}
.page-button {
  zoom: 130%;
}
</style>
