<template>
  <div>
    <Table
      title="Projects"
      :headers="headers"
      :entities="projects"
      @click="viewProjectDetails"
      @addNewEntity="addProject"
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
      return Service.get("projects");
    },
    viewProjectDetails(project){
      this.$router.push(
        { 
          name: "ShowProject", 
          params: { id: project.id } 
        }
    )},
    addProject(){
      this.$router.push({
        name: "AddProject"
      })
    }
  }
}
</script>
