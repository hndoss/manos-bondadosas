import createCollaborator from "@/pages/collaborators/createCollaborator"
import ContactCreate from '../pages/contact/Create'
import ContactUpdate from '../pages/contact/Update'
import ContactShow from '../pages/contact/Show'

export default [
  {
    name: 'ListCollaborator',
    path: '/collaborators/',
    component: ListCollaborator,
    meta: {
      requiresAuth: true
    }
  },
  {
    name: 'CreateCollaborator',
    path: '/collaborators/create',
    component: CreateCollaborator,
    meta: {
      requiresAuth: true
    }
  },
  {
    name: 'UpdateCollaborator',
    path: '/collaborators/edit/:id',
    component: UpdateCollaborator,
    meta: {
      requiresAuth: true
    }
  },
  {
    name: 'ShowCollaborator',
    path: '/collaborators/show/:id',
    component: ShowCollaborator,
    meta: {
      requiresAuth: true
    }
  }
]
