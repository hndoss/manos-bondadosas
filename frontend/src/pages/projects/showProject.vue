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
            <v-col>Project ID: {{ project.id }}</v-col>
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
          :title="project.name + ' Collaborators'"
          :headers="this.person_headers"
          :entities="this.project.collaborators"
          @click="viewCollaboratorDetails"
          @addNewEntity="addCollaborator"
        />
      </v-tab-item>

      <v-tab-item>
        section to add new collaborator to project
        <Table
          title="Beneficiaries"
          :headers="this.person_headers"
          :entities="this.project.beneficiaries"
          @click="viewBeneficiaryDetails"
          @addNewEntity="addBeneficiary"
        />
      </v-tab-item>
      <v-tab-item>
        <Table
          title="Tasks"
          :headers="this.task_headers"
          :entities="this.tasks"
          @click="viewBeneficiaryDetails"
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
    getProject(){
      this.id = this.$route.params.id
      return Service.get(`projects/${this.id}`);
    },
    getCollaborators(){
      return Service.get(`people/collaborators`);
    },
    getTasks(){
      this.id = this.$route.params.id
      return Service.get(`projects/${this.id}/tasks`);
    },
    viewCollaboratorDetails(collaborator){
      this.$router.push(
        { 
          name: "ShowCollaborator", 
          params: { id: collaborator.id } 
        }
    )},
    viewBeneficiaryDetails(beneficiary){
      this.$router.push(
        { 
          name: "ShowBeneficiary", 
          params: { id: beneficiary.id } 
        }
    )},
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
    }
  }
}
</script>
