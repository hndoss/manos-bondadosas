<template>
  <div>
    <v-tabs fixed-tabs background-color="cyan darken-4" dark>
      <v-tab>Information</v-tab>
      <v-tab>Projects</v-tab>
      <v-tab>Events</v-tab>

      <v-tab-item>
        <h1>Id: {{id}}</h1>
      </v-tab-item>

      <v-tab-item>
        <h1>project: {{id}}</h1>
      </v-tab-item>

      <v-tab-item>
        <h1>events: {{id}}</h1>
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
export default {
  name: "ShowCollaborator",
  data() {
    return {
      historyKey: 1,
      id: this.$route.params.id
      // fields: [
      //   {
      //     property: 'value'
      //   },
      //   {
      //     property: 'contactType',
      //     path: 'contactType.name'
      //   },
      //   {
      //     property: 'clients',
      //     type: 'collection',
      //     link: {
      //       route: 'ClientShow'
      //     }
      //   },
      //   {
      //     property: 'companies',
      //     type: 'collection',
      //     link: {
      //       route: 'CompanyShow'
      //     }
      //   }
      // ]
    }
  }
}
</script>
