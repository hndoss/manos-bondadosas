<template>
  <div class="pl-sm-2 pl-md-2 pl-mx-2">
    <h1>{{tittle}}</h1>

    <v-card class="ma-sm-6 ma-md-6 ma-mx-6">
      <v-card-title>
        <v-text-field
          v-model="search"
          append-icon="fas fa-search"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="entities"
        :search="search"
        @click:row="handleEntityClick"
      ></v-data-table>
      <v-col cols="12" sm="10" md="10">
        <v-btn absolute dark fab top left color="red darken-4" @click="handleAddEntityClick">
          <v-icon>mdi-plus</v-icon>
        </v-btn>
      </v-col>
    </v-card>
  </div>
</template>

<script lang="ts">
export default {
  name: "Table",
  props: ["tittle", "headers", "entities"],
  data() {
    return {
      search: "",
    };
  },
  methods: {
    handleEntityClick(row) {
      this.$emit("click", row);
    },
    handleAddEntityClick(){
      this.$emit("addNewEntity")
    }
  },
};
</script>

<style scoped>
.fab-container {
  position: fixed;
  bottom: 0;
  right: 0;
}
</style>