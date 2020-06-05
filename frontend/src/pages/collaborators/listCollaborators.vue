<template>
  <Table
    title="Collaborators"
    :headers="headers"
    :entities="this.collaborators"
    @click="viewCollaboratorDetails"
    @addNewEntity="addCollaborator"
  />
</template>

<script>
import Service from "@/utils/apiService"
import Table from "@/components/table"

export default {
  name: "ListCollaborators",
  components: { Table },
  data () {
    return {
      headers: [
        {
          text: 'id',
          align: 'start',
          filterable: true,
          value: 'id',
        },
        { text: 'First Name', value: 'first_name' },
        { text: 'Last Name', value: 'last_name' },
        { text: 'Age', value: 'age' },
        { text: 'Email', value: 'email' },
      ],
      collaborators: []
    }
  },
  beforeMount() {
    this.getCollaborators()
      .then(data => this.collaborators = data)    
  },
  methods: {
    getCollaborators(){
      return Service.get("people/collaborators");
    },
    viewCollaboratorDetails(collaborator){
      this.$router.push(
        { 
          name: "ShowCollaborator", 
          params: { id: collaborator.id } 
        }
    )},
    addCollaborator(){
      this.$router.push({
        name: "AddCollaborator"
      })
    }
  }
}
</script>
