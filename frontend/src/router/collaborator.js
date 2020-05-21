import ListCollaborators from "@/pages/collaborators/listCollaborators"
import ShowCollaborator from "@/pages/collaborators/showCollaborator"
import AddCollaborator from "@/pages/collaborators/addCollaborator"

export default [
  {
    name: 'ListCollaborators',
    path: '/collaborators/',
    component: ListCollaborators,
    meta: {
      requiresAuth: true
    }
  },
  {
    name: 'ShowCollaborator',
    path: '/collaborators/:id',
    component: ShowCollaborator,
    meta: {
      requiresAuth: true
    }
  },
  {
    name: 'AddCollaborator',
    path: '/collaborators/add',
    component: AddCollaborator,
    meta: {
      requiresAuth: true
    }
  }
]
