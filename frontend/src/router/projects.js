import ListProjects from "@/pages/projects/listProjects"
import ShowProject from "@/pages/projects/showProject"
import AddProject from "@/pages/projects/addProject"
import UpdateProject from "@/pages/projects/updateProject"

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
  },
  {
    name: 'AddProject',
    path: '/add-project',
    component: AddProject,
    meta: {
      requiresAuth: true
    }
  },
  {
    name: 'UpdateProject',
    path: '/update-project/:id',
    component: UpdateProject,
    meta: {
      requiresAuth: true
    }
  }
]
