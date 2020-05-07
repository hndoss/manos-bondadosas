<template>
  <Table tittle="Beneficiaries" :headers="headers" :entities="beneficiaries"/>
</template>

<script>
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
      beneficiaries: [
          {
            id: '0801-1991-123456',
            first_name: "Juan",
            last_name: "Rodríguez",
            age: 24,
            email: "juan.rodriguez@gmail.com",
          },
          {
            id: 'Ice cream sandwich',
            first_name: 237,
            last_name: 9.0,
            age: 37,
            email: 4.3,
          },
          {
            id: 'Eclair',
            first_name: 262,
            last_name: 16.0,
            age: 23,
            email: 6.0,
          },
          {
            id: 'Cupcake',
            first_name: 305,
            last_name: 3.7,
            age: 67,
            email: 4.3,
          },
          {
            id: 'Gingerbread',
            first_name: 356,
            last_name: 16.0,
            age: 49,
            email: 3.9,
          },
          {
            id: 'Jelly bean',
            first_name: 375,
            last_name: 0.0,
            age: 94,
            email: 0.0,
          },
          {
            id: 'Lollipop',
            first_name: 392,
            last_name: 0.2,
            age: 98,
            email: 0,
          },
          {
            id: 'Honeycomb',
            first_name: 408,
            last_name: 3.2,
            age: 87,
            email: 6.5,
          },
          {
            id: 'Donut',
            first_name: 452,
            last_name: 25.0,
            age: 51,
            email: 4.9,
          },
          {
            id: 'KitKat',
            first_name: 518,
            last_name: 26.0,
            age: 65,
            email: 7,
          }
        ],
      }
    },
}
</script>
