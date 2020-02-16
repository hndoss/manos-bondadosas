import Vue from 'vue'
import VueRouter from 'vue-router'
import landing from '@/pages/landing'
import signIn from '@/pages/signin'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: landing
        },
        {
            path: '/signin',
            component: signIn
        }
    ]
})

export default router