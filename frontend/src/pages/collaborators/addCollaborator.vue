<template>
  <div class="ml-sm-4 ml-md-4 ml-lg-4 mr-sm-4 mr-md-4 mr-lg-4">
    <h1>Add New Collaborator</h1>
    <v-form lazy-validation v-model="valid" ref="form">
      <v-row>
        <v-col>
          image
          <!-- <v-img src="@/assets/contact.png" class="grey lighten-2"></v-img> -->
        </v-col>
        <v-col>
          <v-text-field
            v-model="this.collaborator.first_name"
            :counter="60"
            label="Firt Name"
            :rules='this.validator.validateTextField("First Name", 60)'
            class="required"
          ></v-text-field>
          <v-text-field
            v-model="this.collaborator.last_name"
            :counter="60"
            label="Last Name"
            :rules='this.validator.validateTextField("Last Name", 60)'
            class="required"
          ></v-text-field>
          <v-text-field
            v-model="this.collaborator.email"
            :counter="60"
            label="Email"
            :rules="this.validator.validateEmail()"
            class="required"
          ></v-text-field>
          <v-select
            v-model="this.collaborator.sex"
            item-text="Sex"
            :items="sex_options"
            label="Sex"
            :rules='this.validator.validateSelect("Sex")'
            class="required"
          ></v-select>
          <v-text-field
            v-model="age"
            :counter="60"
            label="Age"
            :rules='this.validator.validateSelect("Age")'
            class="required"
          ></v-text-field>
          <!-- Birthday -->
          <!-- <v-date-picker v-model="date" color="green lighten-1" :show-current="false"></v-date-picker> -->
        </v-col>
      </v-row>
      <v-container align="center">
        <v-btn color="success" class="mr-4" @click="saveNewCollaborator">Save</v-btn>
        <v-btn color="error" class="mr-4" @click="cancel">Cancel</v-btn>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import Service from "@/utils/apiService"
import Validator from "@/utils/validator"

export default {
  name: "AddCollaborator",
  data() {
    return {
      id: "", 
      first_name: "",
      last_name: "",
      age: "",
      sex: "",
      sex_options: [ 'Male', 'Female'],
      email: "",
      valid: false,
      validator: Validator
    }
  },
  methods: {
    validate(){
      return this.$refs.form.validate()
    },
    saveNewCollaborator(){
      if(this.validate()){
        let projectId = this.$route.params.project_id
        let collaborator = {
          first_name: this.first_name,
          last_name: this.last_name,
          age: this.age,
          sex: this.sex[0],
          email: this.email,
        }
        if(projectId)
          return Service.post(`projects/${projectId}/collaborators/`, this.collaborator)
            .then(this.$router.go(-1))
        else
          return Service.post(`people/collaborators/`, this.collaborator)
            .then(this.$router.go(-1))
      }
    },
    cancel(){
      this.$router.go(-1)
    }
  }
}
</script>

<style>
</style>