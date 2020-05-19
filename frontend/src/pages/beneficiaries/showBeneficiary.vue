<template>
  <div>
    <v-tabs fixed-tabs background-color="cyan darken-4" dark>
      <v-tab>Information</v-tab>
      <v-tab>Projects</v-tab>
      <v-tab>Tasks</v-tab>
      <v-tab>Report</v-tab>

      <v-tab-item>
        <v-container class="grey lighten-5">
          <v-row>
            <v-col>
              <v-img src="@/assets/contact.png" aspect-ratio="1" class="grey lighten-2"></v-img>
            </v-col>
            <v-col>
              Beneficiary ID: {{ beneficiary.id }}
              <br />
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>

      <v-tab-item>
        <!-- <Table
          tittle="Collaborators"
          :headers="this.headers"
          :entities="this.project.collaborators"
          @click="viewCollaboratorDetails"
        />-->
      </v-tab-item>

      <v-tab-item></v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
import Table from "@/components/layaout/table"
import Service from "@/utils/apiService"

export default {
  name: "ShowBeneficiary",
  components: { Table },
  data() {
    return {
      historyKey: 1,    
      beneficiary: { },
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
    }
  },
  beforeMount() {
    this.getBeneficiary()
      .then(data => this.beneficiary = data)    
  },
  methods: {
    getBeneficiary(){
      let id = this.$route.params.id
      return Service.get(`beneficiaries/${id}`);
    }
  }
}
</script>
