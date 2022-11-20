<template>
  <div>
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

<style>

</style>