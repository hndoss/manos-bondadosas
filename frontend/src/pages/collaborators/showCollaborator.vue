<template>
  <div>
    <v-tabs fixed-tabs background-color="cyan darken-4" dark>
      <v-tab>Information</v-tab>
      <v-tab>Projects</v-tab>
      <v-tab>Events</v-tab>

      <v-tab-item>
        <v-container class="grey lighten-5">
          <v-row>
            <v-col md="2">
              <v-img
                src="@/assets/contact.png"
                aspect-ratio="1"
                class="grey lighten-2"
              ></v-img>
            </v-col>
            <v-col>
              ID: {{ collaborator.id }} <br>
              First Name: {{ collaborator.first_name }} <br>
              Last Name: {{ collaborator.last_name }} <br>
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>

      <v-tab-item>
      </v-tab-item>

      <v-tab-item>
      </v-tab-item>
    </v-tabs>
  </div>
  <!-- <is-show-template
    :fields="fields"
    entity="Contact"
    :history-key="historyKey"
  />-->
</template>

<script>
import Service from "@/utils/apiService"

export default {
  name: "ShowCollaborator",
  data() {
    return {
      historyKey: 1,
      collaborator: { }
    }
  },
  beforeMount() {
    this.getCollaborator()
      .then(data => this.collaborator = data)    
  },
  methods: {
    getCollaborator(){
      let id = this.$route.params.id
      return Service.get(`collaborators/${id}`);
    }
  }
}
</script>
