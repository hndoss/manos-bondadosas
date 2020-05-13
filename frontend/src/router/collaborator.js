import ListCollaborators from "@/pages/collaborators/listCollaborators"
import ShowCollaborator from "@/pages/collaborators/showCollaborator"
// import createCollaborator from "@/pages/collaborators/createCollaborator"

export default [
  {
    name: 'ListCollaborator',
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
  }
  // {
  //   name: 'CreateCollaborator',
  //   path: '/collaborators/create',
  //   component: CreateCollaborator,
  //   meta: {
  //     requiresAuth: true
  //   }
  // },
  // {
  //   name: 'UpdateCollaborator',
  //   path: '/collaborators/edit/:id',
  //   component: UpdateCollaborator,
  //   meta: {
  //     requiresAuth: true
  //   }
  // },

]
