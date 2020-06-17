<template>
  <div>
    <Table
      title="Projects"
      :headers="headers"
      :entities="projects"
      @showEntity="changeRoute('ShowProject', { id: $event.id })"
      @addNewEntity="changeRoute('AddProject')"
      @updateEntity="changeRoute('UpdateProject', { id: $event.id })"
    />
  </div>
</template>

<script>
import Service from "@/utils/apiService"
import Table from "@/components/table"

export default {
  name: "ListProjects",
  components: { Table },
  data () {
    return {
      search: "",
      headers: [
        {
          text: "id",
          align: "start",
          filterable: true,
          value: "id",
        },
        { text: "Name", value: "name" },
        { text: "Description", value: "description" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      projects: []
    }
  },
  beforeMount() {
    this.getProjects()
      .then(data => {
        this.projects = data})
  },
  methods: {
    changeRoute(route, args) {
      this.$router.push(
        {
          name: route,
          params: args
        }
      )
    },
    getProjects(){
      return Service.get("projects");
    }
  }
}
</script>
