<template>
  <div>
    <h1>Detail</h1>
    <!-- <div v-if="video">
      <iframe :src="trailerUrl" frameborder="0"></iframe>
    </div> -->
  <div v-if="trailer.results">
    <iframe :src="videoURI" frameborder="0"></iframe>
  </div>
  <div v-else>
    <h2>트레일러가 없습니다!</h2>
  </div>
  
  
  <p>영화 제목 : {{ movieCard?.title }}</p>
  <p>줄거리 : {{ movieCard?.overview }}</p>
  <p>개봉일 : {{ movieCard?.released_date }}</p>
  <p>장르 : {{ movieCard?.genres }}</p>
  <!-- {{ movieCard?.id }} -->

     <!-- <p>제목 : {{ article?.title }}</p> 
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p> -->
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
const API_KEY = process.env.VUE_APP_API_KEY
export default {
  name: 'MovieDetailView',
  data() {
    return {
      movieCard: null,
      trailer: null,
      
    }
  },
  created() {
    this.getMovieDetail()
    console.log(process.env.VUE_APP_API_KEY)
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
          console.log(res)
          this.movieCard = res.data
          this.movieTrailer()
          
        })
        .catch((err) => {
          console.log(err)
        })
    },
    movieTrailer() {
      console.log(`API_KEY = ${API_KEY}`)
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movieCard.id}/videos?api_key=${API_KEY}&language=ko-KR`,
        // url: `https://api.themoviedb.org/3/movie/436270/videos?api_key=bdc7e9d7c737fde2202d73aceef9477b&language=ko-KR`,
      })
      .then((res) => {
        // console.log(url)
        console.log(res)
        this.trailer = res.data

      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>