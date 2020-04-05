import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: () => import('@/pages/landing')
        },
        {
            path: '/signin',
            component: () => import('@/pages/signin')
        },
        {
            path: '/collaborators',
            component: () => import('@/pages/collaborators')
        },
        {
            path: '/collaborators/add',
            component: () => import('@/pages/collaborators/registerCollaborator')
        },
        {
            path: '/collaborators/:id',
            component: () => import('@/pages/collaborators/viewCollaboratorDetails')
        },
        {
            path: '/benefited',
            component: () => import('@/pages/benefited')
        }
    ]
})

export default router