import ListCollaborators from "@/pages/collaborators/listCollaborators"
import ShowCollaborator from "@/pages/collaborators/showCollaborator"
import AddCollaborator from "@/pages/collaborators/addCollaborator"
import UpdateCollaborator from "@/pages/collaborators/updateCollaborator"

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
    path: '/add-collaborator',
    component: AddCollaborator,
    meta: {
      requiresAuth: true
    }
  },
  {
    name: 'UpdateCollaborator',
    path: '/update-collaborator/:id',
    component: UpdateCollaborator,
    meta: {
      requiresAuth: true
    }
  },
]
