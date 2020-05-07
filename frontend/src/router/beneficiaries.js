import ListBeneficiaries from "@/pages/beneficiaries/listBeneficiaries"
// import createCollaborator from "@/pages/collaborators/createCollaborator"

export default [
  {
    name: 'ListBeneficiaries',
    path: '/beneficiaries/',
    component: ListBeneficiaries,
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
