<template>
    <div class="row d-flex justify-content-center">
        <h1>Main</h1>
    
      <MovieList
      v-for="movieCard in movieCards"
      :key="movieCard.id"
      :movieCard="movieCard"
      class="col-3 m-3"
      />
  
      
      <div>
          <button @click.self="FirstPage">&lt;&lt;</button>
          <button @click.self="FrontPage">&lt;</button>
          <button @click="ChangePage">{{ n1 }}</button>
          <button @click="ChangePage">{{ n2 }}</button>
          <button @click="ChangePage">{{ n3 }}</button>
          <button @click="ChangePage">{{ n4 }}</button>
          <button @click="ChangePage">{{ n5 }}</button>
          <button @click="ChangePage">{{ n6 }}</button>
          <button @click="ChangePage">{{ n7 }}</button>
          <span>
              <button @click.self="BackPage">></button>
              <button @click.self="EndPage">>></button>
          </span>
      </div>
      
    </div>
  
  </template>
  
  <script>
  import MovieList from '@/components/MovieList'
  
  export default {
      name: 'MovieView',
      components: {
          MovieList,
      },
      data() {
          return {
              n1 : 1,
              n2 : 2,
              n3 : 3,
              n4 : 4,
              n5 : 5,
              n6 : 6,
              n7 : 7,
          }
      },
      created: function() {
          this.$store.dispatch('loadMovieCards',1)
      },
      computed: {
          movieCards() {
              // console.log(this.$store.state.movieCards)
              return this.$store.state.movieCards
          },
         
      },
      methods: {
          ChangePage(event) {
              const num = event.target.innerText
              this.$store.dispatch('loadMovieCards', num)
          },
           BackPage() {
              this.n1 += 7, this.n2 += 7, this.n3 += 7, this.n4 += 7
              this.n5 += 7, this.n6 += 7, this.n7 += 7
              this.$store.dispatch('loadMovieCards', this.n1)
          },
          FrontPage() {
              this.n1 -= 7, this.n2 -= 7, this.n3 -= 7, this.n4 -= 7
              this.n5 -= 7, this.n6 -= 7, this.n7 -= 7
              this.$store.dispatch('loadMovieCards', this.n7)
          },
          FirstPage () {
              this.n1 = 1, this.n2 = 2, this.n3 = 3, this.n4 = 4
              this.n5 = 5, this.n6 = 6, this.n7 = 7
              this.$store.dispatch('loadMovieCards', this.n1)
          },
          EndPage () {
              this.n1 = 35911, this.n2 = 35912, this.n3 = 35913, this.n4 = 35914
              this.n5 = 35915, this.n6 = 35916, this.n7 = 35917
              this.$store.dispatch('loadMovieCards', 5000)
          }
          
      }
          
              
  
      
  }
  </script>
  
  <style>
  
  </style>