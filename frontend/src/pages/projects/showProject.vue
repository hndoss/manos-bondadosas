<template>
  <div>
    <v-tabs fixed-tabs background-color="cyan darken-4" dark>
      <v-tab>Information</v-tab>
      <v-tab>Collaborators</v-tab>
      <v-tab>Beneficiaries</v-tab>
      <v-tab>Tasks</v-tab>
      <v-tab>Report</v-tab>

      <v-tab-item>
        <v-container class="grey lighten-5">
          <v-row>
            <v-col>
              <v-img src="@/assets/contact.png" aspect-ratio="1" class="grey lighten-2"></v-img>
            </v-col>
            <v-col>
              Project ID: {{ project.id }}
              <br />
              Description: {{ project.description }}
              <br />
              Direction: {{ project.direction }}
              <br />
              Status: {{ project.status }}
              <br />
              Category: {{ project.category }}
              <br />
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>

      <v-tab-item>
        <Card
          background="projects/collaborate.png"
          instruction="Search for a new collaborator."
          :collection="this.collaborators"
          @saveClick="this.addCollaboratorsToProject"
        ></Card>
        <Table
          title="Project's Collaborators"
          :headers="this.person_headers"
          :entities="this.project.collaborators"
          @showEntity="changeRoute('ShowCollaborator', { id: $event.id })"
          @updateEntity="changeRoute('UpdateCollaborator', { id: $event.id })"
          @addNewEntity="changeRoute('AddCollaborator')"
          @removeEntity="removeCollaborator"
        />
      </v-tab-item>

      <v-tab-item>
        section to add new collaborator to project
        <Table
          title="Beneficiaries"
          :headers="this.person_headers"
          :entities="this.project.beneficiaries"
          @showEntity="changeRoute('ShowBeneficiary', { id: $event.id })"
          @addNewEntity="addBeneficiary"
          @editEntity="editBeneficiary"
        />
      </v-tab-item>
      <v-tab-item>
        <Table
          title="Tasks"
          :headers="this.task_headers"
          :entities="this.tasks"
          @showEntity="changeRoute('ShowBeneficiary', { id: $event.id })"
          @addNewEntity="addTask"
        />
      </v-tab-item>
      <v-tab-item>
        <h1>Reports</h1>
      </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
import Table from "@/components/table"
import Service from "@/utils/apiService"
import Card from "@/components/card"

export default {
  name: "ShowProject",
  components: { Table, Card },
  data() {
    return {
      id: this.$route.params.id,
      project: { },
      tasks: [],
      collaborators: [],
      person_headers: [
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
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      task_headers: [
        {
          text: 'id',
          align: 'start',
          filterable: true,
          value: 'id',
        },
        { text: 'name', value: 'name' },
      ],
    }
  },
  beforeMount() {
    this.getProject()
      .then(data => this.project = data[0])
    this.getTasks()
      .then(data => this.tasks = data)
    this.getCollaborators()
      .then(data => this.collaborators = data)
  },
  methods: {
    changeRoute(route, args){
      this.$router.push(
        { 
          name: route, 
          params: args
        }
      )
    },  
    removeCollaborator(collaborator){
      console.log("removing collaborator from project.")
      Service.delete(`projects/${this.id}/collaborators/`, collaborator.id)
          .then(
            this.getProject()
              .then(data => this.project = data[0])
          )
    },
    getProject(){
      return Service.get(`projects/${this.id}`);
    },
    getCollaborators(){
      return Service.get(`people/collaborators`);
    },
    getTasks(){
      return Service.get(`projects/${this.id}/tasks`);
    },
    addCollaborator(){
      this.$router.push({
        name: "AddCollaboratorToProject",
        params: { project_id: this.$route.params.id }
      })
    },
    addBeneficiary(){
      this.$router.push({
        name: "AddBeneficiary",
        params: { project_id: this.$route.params.id }
      })
    },
    addTask(){
      this.$router.push({
        name: "AddTask",
        params: { project_id: this.$route.params.id } 
      })
    },
    addCollaboratorsToProject(collaborators){
      collaborators.forEach(collaborator_id => {
        let collaborator = {
          "collaborator_id" : collaborator_id
        } 

        Service.post(`projects/${this.id}/collaborators/`, collaborator)
          .then(
            this.getProject()
              .then(data => this.project = data[0])
          )
      });
    },
    editBeneficiary(beneficiary){
      console.log(beneficiary.id)
    }
  }
}
</script>
