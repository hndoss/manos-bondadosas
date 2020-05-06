import Vue from 'vue'
import '@fortawesome/fontawesome-free/css/all.css' 
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

const opts = {
    icons: {
        iconfont: 'fa',
    },
}

export default new Vuetify(opts)