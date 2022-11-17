import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_KEY = "bdc7e9d7c737fde2202d73aceef9477b"
// const API_KEY = process.env.API_KEY

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    articles: [],
    movieCards: [],
    token: null,
    num: 1,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // CHANGE_PAGES: function (state, num) {
      

    // },

    LOAD_MOVIE_CARDS: function(state, results) {
      state.movieCards = results
    },
  
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'ArticleView' })
    },
    GO_LOGIN(state, token) {
      state.token = token
      router.push({ name: 'LogInView' })
    },
  },
  actions: {
    // ChangePage: function(context, num) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/articles/`,       
    //   })
    //   .then((res) => {
    //     context.commit('CHANGE_PAGES', num)
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // },
    loadMovieCards: function (context, num) {
      axios({
        method: 'get',
        // url: `https://api.themoviedb.org/3/movie/popular`,
        url: `${API_URL}/api/v2/movies/`,
        params: {
          api_key: API_KEY,
          language: 'ko-KR',
          page: num,
        }
      })
      .then((response) => {
        console.log(response.data.slice((num-1)*10,(num-1)*10+10))
        context.commit('LOAD_MOVIE_CARDS', response.data.slice((num-1)*10,(num-1)*10+10))
        // context.commit('LOAD_MOVIE_CARDS', response.data.results)
      })
      .catch((error) => {
        console.log(API_KEY)
        console.log(error)
      })
      
    },
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          // console.log(res, context)
          // console.log(res.data)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then(() => {
          context.commit('GO_LOGIN')
        })
    },
  },
  modules: {
  }
})