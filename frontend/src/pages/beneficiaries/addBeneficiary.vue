<template>
  <div class="ml-sm-4 ml-md-4 ml-lg-4 mr-sm-4 mr-md-4 mr-lg-4">
    <h1>Add New Beneficiary</h1>
    <v-form>
      <v-row>
        <v-col>
          image
          <!-- <v-img src="@/assets/contact.png" class="grey lighten-2"></v-img> -->
        </v-col>
        <v-col>
          <v-text-field v-model="first_name" :counter="60" label="Firt Name" required></v-text-field>
          <v-text-field v-model="last_name" :counter="60" label="Last Name" required></v-text-field>
          <v-text-field v-model="email" :counter="60" label="Email" required></v-text-field>
          <v-select v-model="sex" item-text="Sex" :items="sex_options" label="Sex" required></v-select>
          <v-text-field v-model="age" :counter="60" label="Age" required></v-text-field>
          <!-- Birthday -->
          <!-- <v-date-picker v-model="date" color="green lighten-1" :show-current="false"></v-date-picker> -->
        </v-col>
      </v-row>
      <v-container align="center">
        <v-btn :disabled="valid" color="success" class="mr-4" @click="saveNewBeneficiary">Save</v-btn>
        <v-btn color="error" class="mr-4" @click="cancel">Cancel</v-btn>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import Service from "@/utils/apiService"

export default {
  name: "AddBeneficiary",
  data() {
    return {
      id: "", 
      first_name: "",
      last_name: "",
      age: "",
      sex: "",
      sex_options: [ 'Male', 'Female'],
      email: "",
      valid: false
    }
  },
  methods: {
    saveNewBeneficiary(){
      let projectId = this.$route.params.project_id
      let beneficiary = {
        first_name: this.first_name,
        last_name: this.last_name,
        age: this.age,
        sex: this.sex[0],
        email: this.email,
      }
      if(projectId)
        return Service.post(`projects/${projectId}/beneficiaries/`, beneficiary);
      else
        return Service.post(`beneficiaries/`, beneficiary);
    },
    cancel(){
      this.$router.go(-1)
    }
  }
}
</script>

<style>
</style>