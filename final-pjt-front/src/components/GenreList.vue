<template>


  <div class="genre-list">
    <div class="wrap">
      <button @click="goToGenres" class="button"> {{ genre.name }} </button>
    </div>
  </div>
</template>

<script>
// (function() {  
//   ('.btn-6')
//     .on('mouseenter', function(e) {
//       var parentOffset = (this).offset(),
//           relX = e.pageX - parentOffset.left,
//           relY = e.pageY - parentOffset.top;
//       (this).find('span').css({top:relY, left:relX})
//     })
//     .on('mouseout', function(e) {
//       var parentOffset = (this).offset(),
//           relX = e.pageX - parentOffset.left,
//           relY = e.pageY - parentOffset.top;
//       (this).find('span').css({top:relY, left:relX})
//     });
// });
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

/* =============================== */

.genre-list{
  /* float:left; */
  /* margin: 0px 1px 1px 50px; */
  display: inline-block;
  margin: 3px;
}
html, body {
  height: 100%;
}

.wrap {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.button {
  width: 140px;
  height: 45px;
  font-family: 'Roboto', sans-serif;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 500;
  /* color: #000; */
  color: #fff;
  /* background-color: #fff; */
  background-color: #000;
  border: none;
  border-radius: 45px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
  }

.button:hover {
  background-color: #2EE59D;
  /* background-color:rgba(46, 229, 157, 0.4); */
  box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
  color: #fff;
  transform: translateY(-7px);
}
</style>