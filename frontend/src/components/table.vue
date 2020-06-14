<template>
  <div class="pl-sm-2 pl-md-2 pl-mx-2">
    <h1>{{title}}</h1>

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
      <v-data-table :headers="headers" :items="entities" :search="search">
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-2" @click="handleButtonClick('showEntity', item)">mdi-eye</v-icon>
          <v-icon small class="mr-2" @click="handleButtonClick('updateEntity', item)">mdi-pencil</v-icon>
          <v-icon small class="mr-2" @click="handleButtonClick('removeEntity', item)">mdi-delete</v-icon>
        </template>
      </v-data-table>

      <v-col cols="12" sm="10" md="10">
        <v-btn
          absolute
          dark
          fab
          top
          left
          color="red darken-4"
          @click="handleButtonClick('addNewEntity')"
        >
          <v-icon>mdi-plus</v-icon>
        </v-btn>
      </v-col>
    </v-card>
  </div>
</template>

<script lang="ts">
export default {
  name: "Table",
  props: ["title", "headers", "entities"],
  data() {
    return {
      search: "",
    };
  },
  methods: {
    handleButtonClick(emitIdentifier, row) {
      this.$emit(emitIdentifier, row);
    },
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