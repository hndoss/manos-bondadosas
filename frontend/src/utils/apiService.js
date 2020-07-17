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
  },
  patch(url, object) {
    return axios
      .patch(`${VUE_APP_API_URL}/${url}`, object)
      .then(response => response.data)
  }
}

export default Service