<template>
  <div>
    <h1>{{tittle}}</h1>
    <v-card>
      <v-card-title>
        <v-text-field
          v-model="search"
          append-icon="fas fa-search"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table :headers="headers" :items="entities" :search="search" @click:row="handleClick"></v-data-table>
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
    handleClick(row) {
      this.$emit("click", row);
    }
  },
};
</script>

<style scoped>
</style>