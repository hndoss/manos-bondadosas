import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import VS2 from 'vue-script2';
import 'vue-toastr/src/vue-toastr.scss'

Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  VS2,
  render: h => h(App)
}).$mount('#app')
