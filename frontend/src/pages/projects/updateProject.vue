<template>
  <div class="ml-sm-4 ml-md-4 ml-lg-4 mr-sm-4 mr-md-4 mr-lg-4">
    <h1>Update Project</h1>
    <v-form lazy-validation v-model="valid" ref="form">
      <v-row>
        <v-col>
          image
          <!-- <v-img src="@/assets/contact.png" class="grey lighten-2"></v-img> -->
        </v-col>
        <v-col>
          <v-text-field
            v-model="project.name"
            :counter="60"
            label="Name"
            :rules="this.validator.validateTextField('Name', 60)"
            class="required"
          ></v-text-field>

          <v-select
            v-model="project.status"
            item-text="status"
            :items="statuses"
            label="Status"
            :rules="this.validator.validateSelect('Status')"
            class="required"
          ></v-select>

          <v-select
            v-model="project.category"
            item-text="category"
            :items="categories"
            label="Category"
            :rules="this.validator.validateSelect('Category')"
            class="required"
          ></v-select>

          <v-textarea v-model="project.description" color="teal">
            <template v-slot:label>
              <div>
                Description
                <small>(optional)</small>
              </div>
            </template>
          </v-textarea>

          <v-textarea v-model="project.direction" color="teal">
            <template v-slot:label>
              <div>
                Direction
                <small>(optional)</small>
              </div>
            </template>
          </v-textarea>
        </v-col>
      </v-row>
      <v-container align="center">
        <v-btn color="success" class="mr-4" @click="updateProject">Update</v-btn>
        <v-btn color="error" class="mr-4" @click="cancel">Cancel</v-btn>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import Service from "@/utils/apiService"
import Validator from "@/utils/validator"

export default {
  name: "UpdateProject",
  data() {
    return {
      id: this.$route.params.id,
      project: {},
      name: "",
      description: "",
      direction: "",
      status: null,
      category: null,
      categories: [""],
      statuses: [],
      valid: false,
      validator: Validator
    }
  },
  beforeMount() {
    this.getProject().then(data => this.project = data)
    this.getProjectCategories().then(data => this.categories = data)
    this.getProjectStatuses().then(data => this.statuses = data)
  },
  methods: {
    getProjectCategories(){
      return Service.get(`projects/categories`);
    },
    getProjectStatuses(){
      return Service.get(`projects/statuses`);
    },
    validate(){
      return this.$refs.form.validate()
    },
    async getProject(){ return await Service.get(`projects/${this.id}`); },
    updateProject(){
      if(this.validate()){
        delete this.project.collaborators;
        delete this.project.beneficiaries;
        return Service.patch(`projects/${this.id}/`, this.project);
      }
    },
    cancel(){
      this.$router.go(-1) 
    }
  }
}
</script>

<style>
.required label::before {
  content: "*";
}
</style>