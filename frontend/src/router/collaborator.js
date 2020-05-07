import ListCollaborators from "@/pages/collaborators/listCollaborators"
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
  // {
  //   name: 'ShowCollaborator',
  //   path: '/collaborators/show/:id',
  //   component: ShowCollaborator,
  //   meta: {
  //     requiresAuth: true
  //   }
  // }
]
