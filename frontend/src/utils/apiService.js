import axios from 'axios'
// import axios from '../interceptor'

import { VUE_APP_API_URL } from "@/config/variables"

const Service = {
  get(url, query) {
    if (query)
      return axios
        .get(`${VUE_APP_API_URL}/${url}?${query}`)
        .then(response => {
          return response.data
        })
    else
      return axios
        .get(`${VUE_APP_API_URL}/${url}`)
        .then(response => {
          return response.data
        })
  },
  post(url, object) {
    return axios
      .post(`${VUE_APP_API_URL}/${url}`, object)
      .then(response => response.data)
  }
}

export default Service

// export const update = ({ commit, state }, namespace) => {
//   commit(`${namespace}_SET_ERROR`, null)

//   return axios
//     .put(
//       `${API_HOST}/${pluralize(namespace.toLowerCase())}/${state.item.id}`,
//       state.item
//     )
//     .then(response => response.data)
//     .catch(e => {
//       const { data } = e.response

//       if (data.violations) {
//         const errors = {}

//         data.violations.map(violation => {
//           Object.assign(errors, { [violation.propertyPath]: violation.message })
//         })

//         commit(`${namespace}_SET_ERRORS`, errors)
//       }

//       const error = data['hydra:description']
//         ? data['hydra:description']
//         : data.message
//       commit(`${namespace}_SET_ERROR`, error)

//       throw data
//     })
// }

// export const remove = ({ commit }, namespace, item) =>
//   axios
//     .delete(`${API_HOST}/${pluralize(namespace.toLowerCase())}/${item.id}`)
//     .catch(e => {
//       const message =
//         e.response.status === 409
//           ? 'Not possible to remove. This record has relations.'
//           : e.message

//       commit(`${namespace}_SET_ERROR`, message)

//       throw e
//     })

// export const reset = ({ commit }, namespace) => {
//   commit(`${namespace}_RESET`)
// }
