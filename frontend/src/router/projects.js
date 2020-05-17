import ListProjects from "@/pages/projects/listProjects"
import ShowProject from "@/pages/projects/showProject"

export default [
  {
    name: 'ListProjects',
    path: '/projects/',
    component: ListProjects,
    meta: {
      requiresAuth: true
    }
  },
  {
    name: 'ShowProject',
    path: '/projects/:id',
    component: ShowProject,
    meta: {
      requiresAuth: true
    }
  }
]
