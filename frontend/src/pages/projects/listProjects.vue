<template>
  <Table tittle="Projects" :headers="headers" :entities="projects" />
</template>

<script>
import Service from "@/utils/apiService"
import Table from "@/components/layaout/table"

export default {
  name: "ListProjects",
  components: { Table },
  data () {
    return {
      search: '',
      headers: [
        {
          text: 'id',
          align: 'start',
          filterable: true,
          value: 'id',
        },
        { text: 'Name', value: 'name' },
        { text: 'Description', value: 'description' },
      ],
      projects: [],
    }
  },
  beforeMount() {
    this.getProjects()
      .then(data => this.projects = data)
  },
  methods: {
    getProjects(){
      return Service.getItems("projects");
    }
  }
}
</script>
