import Vue from 'vue';
import VueRouter from 'vue-router';
import landing from '@/pages/landing';
import signIn from '@/pages/signin';
import collaborators from '@/pages/collaborators';
import registerCollaborator from '@/pages/collaborators/registerCollaborator';
import viewCollaboratorDetails from '@/pages/collaborators/viewCollaboratorDetails';
import benefited from '@/pages/benefited';


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
            path: '/collaborators',
            component: collaborators
        },
        {
            path: '/collaborators/add',
            component: registerCollaborator
        },
        {
            path: '/collaborators/:id',
            component: viewCollaboratorDetails
        },
        {
            path: '/benefited',
            component: benefited
        }
    ]
})

export default router