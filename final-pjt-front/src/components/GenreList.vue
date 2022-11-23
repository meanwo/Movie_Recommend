<header>
  <link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet">
 <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500&display=swap" rel="stylesheet">
</header>
<template>
  
  <div class="genre-list">
    <div class="frame">
      <button @click="goToGenres" class="custom-btn btn-10"> {{ genre.name }} </button>
    </div>
  </div>
</template>

<script>
(function() {  
  ('.btn-6')
    .on('mouseenter', function(e) {
      var parentOffset = (this).offset(),
          relX = e.pageX - parentOffset.left,
          relY = e.pageY - parentOffset.top;
      (this).find('span').css({top:relY, left:relX})
    })
    .on('mouseout', function(e) {
      var parentOffset = (this).offset(),
          relX = e.pageX - parentOffset.left,
          relY = e.pageY - parentOffset.top;
      (this).find('span').css({top:relY, left:relX})
    });
});
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
.frame {
  width: 90%;
  margin: 40px auto;
  text-align: center;
}
button {
  margin: 20px;
  outline: none;
}
.custom-btn {
  width: 130px;
  height: 40px;
  padding: 10px 25px;
  border: 2px solid #000;
  
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
}
.btn-10 {
  transition: all 0.3s ease;
  overflow: hidden;


}
.btn-10:after {
  position: absolute;
  content: " ";
  top: 0;
  left: 0;
  z-index: -1;
  width: 100%;
  height: 100%;
  transition: all 0.3s ease;
  -webkit-transform: scale(.1);
  transform: scale(.1);
  
}
.btn-10:hover {
  color: #fff;
  /* color:#000; */
  
}
.btn-10:hover:after {
  background: #000;
  /* background:#eeeeee; */
  -webkit-transform: scale(1);
  transform: scale(1);
  /* background:#fff; */

}

/*  */

@import url(https://fonts.googleapis.com/css?family=Open+Sans:400|Raleway:300);
html {
  padding-top: 50px;
  font-family: "Open Sans", Helvetica, arial, sans-serif;
  text-align: center;
  background-color: #eeeeee;
}
html *,
html *:before,
html *:after {
  box-sizing: border-box;
  transition: 0.5s ease-in-out;
}
html i, html em,
html b, html strong,
html span {
  transition: none;
}

*:before,
*:after {
  z-index: -1;
}

h1,
h4 {
  font-family: "Raleway", "Open Sans", sans-serif;
  margin: 0;
  line-height: 1;
}

a {
  text-decoration: none;
  line-height: 80px;
  color: black;
}

.centerer {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  padding: 0 1rem;
}

@media (min-width: 600px) {
  .wrap {
    width: 50%;
    /* height: 50%; */
    float: left;
  }
}
[class^=btn-] {
  position: relative;
  display: block;
  overflow: hidden;
  width: 100%;
  height: 80px;
  max-width: 250px;
  margin: 1rem auto;
  text-transform: uppercase;
  border: 1px solid currentColor;
}
.genre-list{
  /* float:left; */
  /* margin: 0px 1px 1px 50px; */
  display: inline-block;
  margin: 3px;

}
.btn-6 {
  color: #29585e;
  height: 50%;
}
.btn-6 span {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-radius: 50%;
  background-color: #29585e;
  transition: width 0.4s ease-in-out, height 0.4s ease-in-out;
  transform: translate(-50%, -50%);
  z-index: -1;
}
.btn-6:hover {
  color: #c0ced0;
}
.btn-6:hover span {
  width: 225%;
  height: 562.5px;
}
.btn-6:active {
  background-color: #29585e;
}
</style>