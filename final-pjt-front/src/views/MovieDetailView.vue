<template>
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

    <div class="detail-fade-in text-light p-3 container detail-page-txt">
      <h4>영화 제목 : {{ movieCard?.title }}</h4>
      <h4>평점: &emsp;{{ movieCard?.vote_avg }}</h4>
      <br />
      <h4 class="movie-overview">줄거리 : {{ movieCard?.overview }}</h4>
      <p>개봉일 : {{ movieCard?.released_date }}</p>
      <br />
      <GenreList
        v-for="(genre, index) in movieCard.genres"
        :key="index"
        :genre="genre"
      />
    </div>
    <button @click="ChangePage" class="mb-3">back</button>
    <RecommendList :movie-card="movieCard" />
    <CommentForm @create-comment="createComment" :movie-card="movieCard" />
    <CommentList
      :comments="comments"
      :movie-card="movieCard"
      class="comment-list"
    />
  </div>
</template>

<script>
import axios from "axios";
import GenreList from "@/components/GenreList";
import RecommendList from "@/components/RecommendList";
import CommentForm from "@/components/CommentForm";
import CommentList from "@/components/CommentList";

// 유튜브 주소 + API_KEY
const YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search";
// const YOUTUBE_API_KEY = 'AIzaSyCpoA4AXknB1SOqIn2S5wUbevdmMtOb22M'
const YOUTUBE_API_KEY = "";
// const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

const API_URL = "http://127.0.0.1:8000";
export default {
  name: "MovieDetailView",
  components: {
    GenreList,
    CommentForm,
    CommentList,
    RecommendList,
  },
  data() {
    const base_url = "https://image.tmdb.org/t/p/original";
    return {
      movieCard: {},
      trailer: [],
      base_url,
      comments: [],
    };
  },
  created() {
    window.scrollTo({ top: 0, behavior: "smooth" });
    this.getMovieDetail();
  },
  computed: {
    videoURI() {
      const trailerVideo = this.trailer;
      return `https://www.youtube.com/embed/${trailerVideo}`;
    },
  },

  methods: {
    createComment(res) {
      console.log(res);
      this.comments.push(res.data);
    },
    getComments() {
      axios({
        method: "get",
        url: `${API_URL}/api/v2/comments/list/${this.movieCard.id}/`,
      }).then((res) => {
        this.comments = res.data;
        console.log(this.comments);
      });
    },
    getMovieDetail() {
      axios({
        method: "get",
        url: `${API_URL}/api/v2/movies/${this.$route.params.id}`,
      })
        .then((res) => {
          this.movieCard = res.data;
          this.movieTrailer();
          this.getComments();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    ChangePage(event) {
      console.log(event);
    },
    movieTrailer() {
      axios
        .get(YOUTUBE_API_URL, {
          params: {
            key: YOUTUBE_API_KEY,
            type: "video",
            part: "snippet",
            q: `${this.movieCard.title} 예고편`,
          },
        })
        .then((res) => {
          this.trailer = res.data.items[0].id.videoId;
        })
        .catch((err) => {
          console.log(err, "에러발생!");
        });
    },
  },
};
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&display=swap");
.front {
  zoom: 90%;
  position: relative;
  z-index: 1;
}
.background-img {
  opacity: 0.4;
  position: absolute;
  top: 20%;
  left: 50%;
  z-index: -1;

  width: 55%;

  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  transform: translate(-50%, -20%);

  animation: fadeout 0.5s;
}
.detail-fade-in {
  animation: fadein cubic-bezier(0.55, 0.055, 0.675, 0.19);
}
@keyframes fadeout {
  from {
    opacity: 1;
  }
  to {
    opacity: 1;
  }
}
@keyframes fadein {
  from {
    opacity: -1;
  }
  to {
    opacity: 1;
  }
}
.detail-page-txt {
  font-family: "Noto Sans KR", sans-serif;
  display: block;
  width: 1100px;
}
.movie-overview {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  line-height: 1.2;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  word-spacing: 5px;
}
.comment-list {
  display: block;
}
</style>
