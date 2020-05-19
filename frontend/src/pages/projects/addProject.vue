<template>
  <div class="ml-sm-4 ml-md-4 ml-lg-4 mr-sm-4 mr-md-4 mr-lg-4">
    <h1>Add New Project</h1>
    <v-form>
      <v-row>
        <v-col>
          image
          <!-- <v-img src="@/assets/contact.png" class="grey lighten-2"></v-img> -->
        </v-col>
        <v-col>
          <v-text-field v-model="name" :counter="60" label="Name" required></v-text-field>
          <v-select v-model="status" item-text="status" :items="statuses" label="Status" required></v-select>
          <v-select
            v-model="category"
            item-text="category"
            :items="categories"
            label="Category"
            required
          ></v-select>
          <v-textarea v-model="description" color="teal">
            <template v-slot:label>
              <div>
                Description
                <small>(optional)</small>
              </div>
            </template>
          </v-textarea>
          <v-textarea v-model="direction" color="teal">
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
        <v-btn :disabled="valid" color="success" class="mr-4" @click="saveNewProject">Save</v-btn>
        <v-btn color="error" class="mr-4" @click="cancel">Cancel</v-btn>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import Service from "@/utils/apiService"

export default {
  name: "AddProject",
  data() {
    return {
      name: "",
      description: "",
      direction: "",
      status: null,
      category: null,
      categories: [""],
      statuses: [],
      valid: false
    }
  },
  beforeMount() {
    this.getProjectCategories()
      .then(data => this.categories = data)
    this.getProjectStatuses()
      .then(data => this.statuses = data)
  },
  methods: {
    getProjectCategories(){
      return Service.get(`projects/categories`);
    },
    getProjectStatuses(){
      return Service.get(`projects/statuses`);
    },
    saveNewProject(){
      let project = {
        name: this.name,
        description: this.description,
        direction: this.direction,
        status: this.status,
        category: this.category,
      }
      return Service.post(`projects/`, project);
    },
    cancel(){
      this.$router.push({
        name: "ListProjects"
      })
    }
  }
}
</script>

<style>
</style>