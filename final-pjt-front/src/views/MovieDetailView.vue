<template>
<<<<<<< HEAD
  <div class="front p-3 mb-2 bg-dark">
    <h1 class="text-light p-3">{{ movieCard.title }}</h1>
    <img
      :src="base_url + movieCard.poster_path"
      alt="영화이미지"
      class="background-img"
    />

    <!-- TMDB API일 때 -->
    <!-- <div v-if="trailer.results" class="embed-responsive embed-responsive-21by9"> -->

    <!-- 유튜브 API일 때 -->
    <!-- <iframe class="embed-responsive-item" width="850" height="550" :src="videoURI" frameborder="0"></iframe> -->

    <div v-if="trailer" class="embed-responsive embed-responsive-21by9">
      <iframe
        class="embed-responsive-item detail-fade-in"
        width="850"
        height="550"
        :src="videoURI"
        frameborder="0"
      ></iframe>
    </div>
    <div v-else>
      <h2>트레일러가 없습니다!</h2>
    </div>

    <div class="detail-fade-in text-light p-3 container">
      <!-- <p>{{ movieCard?.poster_path }}</p> -->
      <p>영화 제목 : {{ movieCard?.title }}</p>
      <p>평점: &emsp;{{ movieCard?.vote_avg }}</p>
      <p>줄거리 : {{ movieCard?.overview }}</p>
      <p>개봉일 : {{ movieCard?.released_date }}</p>
      <p>장르 : {{ movieCard?.genres }}</p>
      -->
      {{ movieCard?.id }}
      <br />
      <GenreList
        v-for="(genre, index) in movieCard.genres"
        :key="index"
        :genre="genre"
      />
      <button @click="ChangePage">back</button>
    </div>
    
    <CommentForm :movie-card="movieCard"/>
    <CommentList :movie-card="movieCard"/>
    {{comments}}
=======
  <div>
    <h1>Detail</h1>
    <div class="">
      <img :src="base_url+movieCard.poster_path" alt="영화이미지" class="background-img">
    </div>
  
    <div v-if="trailer.results" class="embed-responsive embed-responsive-21by9">
      <iframe class="embed-responsive-item" width="850" height="550" :src="videoURI" frameborder="0"></iframe>
    </div>
    <div v-else>
      <h2>트레일러가 없습니다!</h2>
    </div>
    
    <p>{{ movieCard.poster_path }}</p>
    <p>영화 제목 : {{ movieCard?.title }}</p>
    <p>줄거리 : {{ movieCard?.overview }}</p>
    <p>개봉일 : {{ movieCard?.released_date }}</p>

    <GenreList v-for="(genre, index) in movieCard.genres" :key="index" :genre="genre">
      <!-- <button @click="goToGenres"> {{ genre.name }} </button>  -->
    </GenreList>
>>>>>>> c718f2e78a17277d28f1b63038b27e9146baf9bd
  </div>
</template>

<script>
<<<<<<< HEAD
import axios from "axios";
import GenreList from "@/components/GenreList"
import CommentForm from '@/components/CommentForm'
import CommentList from '@/components/CommentList'

// 유튜브 주소 + API_KEY
const YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search";
// const YOUTUBE_API_KEY = 'AIzaSyCpoA4AXknB1SOqIn2S5wUbevdmMtOb22M'
const YOUTUBE_API_KEY = "";

const API_URL = "http://127.0.0.1:8000";
// const API_KEY = 'bdc7e9d7c737fde2202d73aceef9477b'
// const API_KEY = process.env.VUE_APP_API_KEY
export default {
  name: "MovieDetailView",
  components: {
    GenreList,
    CommentForm,
    CommentList,
  },
  data() {
    const base_url = "https://image.tmdb.org/t/p/original";
=======
import axios from 'axios'
import GenreList from '@/components/GenreList'

const API_URL = 'http://127.0.0.1:8000'
// const API_KEY = 'bdc7e9d7c737fde2202d73aceef9477b'
const API_KEY = process.env.VUE_APP_API_KEY
export default {
  name: 'MovieDetailView',
  components: {
          GenreList,
      },
  data() {
    const base_url = 'https://image.tmdb.org/t/p/original/'
>>>>>>> c718f2e78a17277d28f1b63038b27e9146baf9bd
    return {
      movieCard: '',
      trailer: [],
      base_url,
<<<<<<< HEAD
      comments: [],
    };
=======
      // genreList : null,
      
    }
>>>>>>> c718f2e78a17277d28f1b63038b27e9146baf9bd
  },
  created() {
    window.scrollTo({ top: 0, behavior: "smooth" });
    this.getMovieDetail()
<<<<<<< HEAD
    // console.log(process.env.VUE_APP_API_KEY)
    // console.log("트레일러.리절트",this.trailer.results)
=======
    console.log(this.movieCard.genres)
    // console.log(process.env.VUE_APP_API_KEY)
    // this.getGenreList()
>>>>>>> c718f2e78a17277d28f1b63038b27e9146baf9bd
  },
  computed: {
    videoURI() {
      // console.log(this.trailer)
      const trailerVideo = this.trailer;
      // console.log(trailerVideo)
      return `https://www.youtube.com/embed/${trailerVideo}`;
    },
    getNewComments() {
      return this.comments
    }
  },

  methods: {
    getComments() { 
        axios({
          method: 'get',
          url: `${API_URL}/api/v2/comments/list/${this.movieCard.id}/`
          
        })
          .then((res) => {
            // console.log(res)
            this.comments = res.data;
            console.log(this.comments)
          })
      },
    getMovieDetail() {
      axios({
        method: "get",
        url: `${API_URL}/api/v2/movies/${this.$route.params.id}`,
      })
        .then((res) => {
          this.movieCard = res.data;
          // console.log(this.movieCard)
          this.movieTrailer()
          this.getComments();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    ChangePage(event) {
      console.log(event);
      // const num = event.target.innerText
      // this.$store.dispatch('loadMovieCards', num)
      // this.$router.push({ name: 'MainView', params: {id: num } })
    },
    movieTrailer() {
      // console.log(`API_KEY = ${API_KEY}`)
      axios
        .get(YOUTUBE_API_URL, {
          params: {
            key: YOUTUBE_API_KEY,
            type: "video",
            part: "snippet",
            q: `${this.movieCard.title} 예고편`,
            // q: '어벤져스 예고편'
          },
        })
        .then((res) => {
          // console.log(res.data)
          this.trailer = res.data.items[0].id.videoId;
          // console.log(this.trailer)
        })
        .catch((err) => {
          console.log(err, "에러발생!");
        });

<<<<<<< HEAD
      // axios({
      //   method: 'get',
      //   url: `https://api.themoviedb.org/3/movie/${this.movieCard.id}/videos?api_key=${API_KEY}&language=ko-KR`,
      //   // url: `https://api.themoviedb.org/3/movie/436270/videos?api_key=bdc7e9d7c737fde2202d73aceef9477b&language=ko-KR`,
      // })
      // .then((res) => {
      //   // console.log(url)
      //   console.log(res.data)
      //   this.trailer = res.data
      // })
      // .catch((err) => {
      //   console.log(err)
      // })
    },
  },
};
</script>
<style scoped>
.front {
  /* width: 100%;
  height: 100%; */
  /* text-align: center; */
  position: relative;
  z-index: 1;
  /* font-size: 1rem; */
  /* display: inline-block; */
}
.background-img {
  width: 80%;
  opacity: 0.4;
  position: absolute;
  top: 50%;
  left: 50%;
  z-index: -1;
  display: flex;
  justify-content: center;
  align-items: center;
  transform: translate(-50%, -20%);
  /* transform: scale(1.8); */
  /* animation: scaleImage 5s ease-out forwards; */
  animation: fadeout 1s;
  /* -webkit-animation: fadeout 4s; */
}
.detail-fade-in {
  animation: fadein 1s;
}
@keyframes fadeout {
  from {
    opacity: 1;
  }
  to {
    opacity: 1;
=======
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToGenres() {
      console.log()
        // this.$router.push({ name: 'GenresView', params: {}})
      }
    }
>>>>>>> c718f2e78a17277d28f1b63038b27e9146baf9bd
  }

</script>
<style scoped>
.background-img {
  float: left;
  margin: 0 auto;
  opacity: 10;
}
<<<<<<< HEAD
@keyframes fadein {
  from {
    opacity: -1;
  }
  to {
    opacity: 1;
  }
}
</style>
=======

</style>
>>>>>>> c718f2e78a17277d28f1b63038b27e9146baf9bd
