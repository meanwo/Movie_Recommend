<template>
  <div>
    <h1>Detail</h1>
      <div class="front">
        <img :src="base_url+movieCard.poster_path" alt="영화이미지" class="background-img">
            
      
  
  <div v-if="trailer.results" class="embed-responsive embed-responsive-21by9">
    <iframe class="embed-responsive-item" width="850" height="550" :src="videoURI" frameborder="0"></iframe>
  </div>
  <div v-else>
    <h2>트레일러가 없습니다!</h2>
  </div>
  
  <p>{{ movieCard?.poster_path }}</p>
  <p>영화 제목 : {{ movieCard?.title }}</p>
  <p>줄거리 : {{ movieCard?.overview }}</p>
  <p>개봉일 : {{ movieCard?.released_date }}</p>
  <p>장르 : {{ movieCard?.genres }}</p> -->
    {{ movieCard?.id }}
    <br>
  <button @click="ChangePage">back</button>

     <!-- <p>제목 : {{ article?.title }}</p> 
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p> -->
   </div> 
  </div>
</template>

<script>
import axios from 'axios'

// 유튜브 주소 + API_KEY
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_API_KEY = 'AIzaSyCpoA4AXknB1SOqIn2S5wUbevdmMtOb22M'

const API_URL = 'http://127.0.0.1:8000'
// const API_KEY = 'bdc7e9d7c737fde2202d73aceef9477b'
// const API_KEY = process.env.VUE_APP_API_KEY
export default {
  name: 'MovieDetailView',
  data() {
    const base_url = 'https://image.tmdb.org/t/p/original'
    return {
      movieCard: '',
      trailer: [],
      base_url
      
    }
  },
  created() {
    this.getMovieDetail()
    // console.log(process.env.VUE_APP_API_KEY)
    // console.log("트레일러.리절트",this.trailer.results)
  },
  computed: {
    videoURI () {
      const trailer = this.trailer.results[0].key
      return `https://www.youtube.com/embed/${trailer}`
    }
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/movies/${this.$route.params.id}`
      })
        .then((res) => {
          this.movieCard = res.data
          // console.log(this.movieCard)
          this.movieTrailer()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    ChangePage(event) {
          console.log(event)
          // const num = event.target.innerText
          // this.$store.dispatch('loadMovieCards', num)
          // this.$router.push({ name: 'MainView', params: {id: num } })
      },
    movieTrailer() {
      // console.log(`API_KEY = ${API_KEY}`)
      axios.get(YOUTUBE_API_URL, {
        params: {
          key : YOUTUBE_API_KEY,
          type: 'video',
          part: 'snippet',
          // q: `${this.movieCard.title} 예고편`
          q: '어벤져스 예고편'
        }
      }) .then((res) => {
        console.log(res)
        this.trailer = res.data.items[0]
      }) .catch((err) => {

        console.log(err, '에러발생!')
      })

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
    }
  }
}
</script>
<style scoped>
.front {
  /* width: 100%;
  height: 100%; */
  /* text-align: center; */
  position: relative;
  z-index: 1;
  /* font-size: 1rem; */
  position: absolute;
}
.background-img {
  /* width: 100%;
  height: 100%; */
  
  /* float: left; */
  opacity: 0.4;
  position: absolute;
  z-index: -1;
  margin: 0 auto; 
  display: block;
}

</style>