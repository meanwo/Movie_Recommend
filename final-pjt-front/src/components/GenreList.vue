<template>
  <div class="genre-list">
    <div class="wrap">
      <button @click="goToGenres" class="button">{{ genre.name }}</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "GenreList",
  data() {
    return {};
  },
  props: {
    genre: Object,
  },
  methods: {
    goToGenres() {
      this.$router.push({
        name: "GenreDetailView",
        params: { id: this.genre.id, genreName: this.genre.name },
      });
    },
  },
};
</script>

<style scoped>
.genre-list {
  display: inline-block;
  margin: 5px;
}
html,
body {
  height: 100%;
}

.wrap {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.button {
  width: 150px;
  height: 55px;
  font-family: "Roboto", sans-serif;
  font-size: 16px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 500;
  color: #fff;
  background-color: #505050;
  border: none;
  border-radius: 45px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
}

.button:hover {
  background-color: #2ee59d;
  box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
  color: #fff;
  transform: translateY(-7px);
}
</style>
