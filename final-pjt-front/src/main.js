import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import ToggleButton from 'vue-js-toggle-button'
import { BootstrapVue } from 'bootstrap-vue'

// Import Bootstrap and BootstrapVue CSS files (order is important) 
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(ToggleButton)
Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
