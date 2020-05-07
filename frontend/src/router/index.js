import Vue from 'vue';
import VueRouter from 'vue-router';
import collaboratorRoutes from "./collaborator"
import beneficiariesRoutes from "./beneficiaries"

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: () => import('@/components/layaout/mainSlot'),
            children: [
                ...collaboratorRoutes,
                ...beneficiariesRoutes
            ]
        }
    ]
})

export default router