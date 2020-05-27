import Vue from 'vue';
import VueRouter from 'vue-router';
import MainSlot from '@/components/layaout/mainSlot'
import Dashboard from '@/pages/dashboard'
import Calendar from '@/pages/calendar'
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
                {
                    name: 'Dashboard',
                    path: '/dashboard',
                    component: Dashboard,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    name: 'Calendar',
                    path: '/calendar',
                    component: Calendar,
                    meta: {
                        requiresAuth: true
                    }
                },
                ...collaboratorRoutes,
                ...beneficiariesRoutes,
                ...projects,
            ]
        }
    ]
})

export default router