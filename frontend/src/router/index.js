import Vue from 'vue';
import VueRouter from 'vue-router';
import MainSlot from '@/components/layaout/mainSlot'
import collaboratorRoutes from "./collaborator"
import beneficiariesRoutes from "./beneficiaries"
import projects from "./projects"

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'hash',
    routes: [
        {
            path: '/',
            component: MainSlot,
            children: [
                ...collaboratorRoutes,
                ...beneficiariesRoutes,
                ...projects,
            ]
        }
    ]
})

export default router