<template>
  <div class="ml-sm-4 ml-md-4 ml-lg-4 mr-sm-4 mr-md-4 mr-lg-4">
    <h1>Add New Collaborator</h1>
    <v-form>
      <v-row>
        <v-col>
          image
          <!-- <v-img src="@/assets/contact.png" class="grey lighten-2"></v-img> -->
        </v-col>
        <v-col>
          <v-text-field v-model="first_name" :counter="60" label="Firt Name" required></v-text-field>
          <v-text-field v-model="last_name" :counter="60" label="Last Name" required></v-text-field>
          <v-select v-model="age" :items="ages" label="Age" required></v-select>
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
        <v-btn :disabled="valid" color="success" class="mr-4" @click="saveNewCollaborator">Save</v-btn>
        <v-btn color="error" class="mr-4" @click="cancel">Cancel</v-btn>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import Service from "@/utils/apiService"

export default {
  name: "AddCollaborator",
  data() {
    return {
      first_name: "",
      last_name: "",
      age: "",
      status: null,
      sex: null,
      email: "",
      valid: false
    }
  },
  methods: {
    saveNewCollaborator(){
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
        name: "ListCollaborators"
      })
    }
  }
}
</script>

<style>
</style>