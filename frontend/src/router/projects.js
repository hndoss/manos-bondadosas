import ListProjects from "@/pages/projects/listProjects"

export default [
  {
    name: 'ListProjects',
    path: '/projects/',
    component: ListProjects,
    meta: {
      requiresAuth: true
    }
  },
]
