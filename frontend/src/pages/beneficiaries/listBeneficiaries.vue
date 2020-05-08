<template>
  <Table tittle="Beneficiaries" :headers="headers" :entities="beneficiaries" />
</template>

<script>
import Service from "@/utils/apiService"
import Table from "@/components/layaout/table"

export default {
  name: "ListBeneficiaries",
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
        { text: 'First Name', value: 'first_name' },
        { text: 'Last Name', value: 'last_name' },
        { text: 'Age', value: 'age' },
        { text: 'Email', value: 'email' },
      ],
      beneficiaries: [],
    }
  },
  beforeMount() {
    this.getBeneficiaries()
      .then(data => this.beneficiaries = data)
  },
  methods: {
    getBeneficiaries(){
      return Service.getItems("beneficiaries");
    }
  }
}
</script>
