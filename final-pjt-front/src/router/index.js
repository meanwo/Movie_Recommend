import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '@/views/ArticleView'
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import MainView from '@/views/MainView'
import MovieDetailView from '@/views/MovieDetailView'
import GenreDetailView from '@/views/GenreDetailView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'ArticleView',
    component: ArticleView
  },
 
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },

  {
    path: '/movies/:id',
    name: 'MovieDetailView',
    component: MovieDetailView,
  },
  {
    // path: '/main/:id',
    path: '/main',
    name: 'MainView',
    component: MainView,
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },
  {
<<<<<<< HEAD
    path:'/genre/:id',
=======
    path: '/genre/:id',
>>>>>>> c718f2e78a17277d28f1b63038b27e9146baf9bd
    name: 'GenreDetailView',
    component: GenreDetailView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
