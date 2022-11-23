<template>
  <div class="genre-list">
    
      <button @click="goToGenres"> {{ genre.name }} </button>
    
  </div>
</template>

<script>
export default {
    name: 'GenreList',
    data() {
      return {

      }
    },
    props: {
        genre: Object,
    },
    methods: {
        goToGenres() {
            // console.log(this.genre.id)
            this.$router.push({ name: 'GenreDetailView', params: {id:this.genre.id, genreName: this.genre.name}})
        }
    }
    
}
</script>

<style scoped>
.genre-list{
  /* float:left; */
  /* margin: 0px 1px 1px 50px; */
  display: inline-block;
  margin: 1px;
}

</style>