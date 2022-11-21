<template>
  <div>
    <button @click="goToGenres"> {{ genre.name }} </button>
  </div>
</template>

<script>
export default {
<<<<<<< HEAD
    name: 'GenreList',
    data() {
      return {

      }
    },
=======

    name: 'GenreList',
>>>>>>> c718f2e78a17277d28f1b63038b27e9146baf9bd
    props: {
        genre: Object,
    },
    methods: {
        goToGenres() {
<<<<<<< HEAD
            // console.log(this.genre.id)
            this.$router.push({ name: 'GenreDetailView', params: {id:this.genre.id, genreName: this.genre.name}})
        }
    }
    
=======
            console.log(this.genre.id)
            this.$router.push({ name: 'GenreDetailView', params: {id: this.genre.id }})
        }
    }
>>>>>>> c718f2e78a17277d28f1b63038b27e9146baf9bd
}
</script>

<style>

</style>