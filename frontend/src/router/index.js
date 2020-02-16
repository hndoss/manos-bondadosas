import Vue from 'vue';
import VueRouter from 'vue-router';
import landing from '@/pages/landing';
import signIn from '@/pages/signin';
import about from '@/pages/about'


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
        },
        {
            path: '/about',
            component: about
        }
    ]
})

export default router