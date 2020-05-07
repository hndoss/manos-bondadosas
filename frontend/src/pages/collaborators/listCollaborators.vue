<template>
  <Table tittle="Collaborators" :headers="headers" :entities="collaborators" />
</template>

<script>
import Service from "@/utils/apiService"
import Table from "@/components/layaout/table"

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
    }
  },
  computed: {
    collaborators(){
      return this.getCollaborators();
    }
  },
  methods: {
    getCollaborators(){
      return Service.getItems("collaborators");

    }
  }
}
</script>
