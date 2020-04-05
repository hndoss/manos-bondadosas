<template>
  <div>
    <h1>Collaborators</h1>SEARCH BAR
    <v-container class="my-5">
      <v-layout row wrap>
        <v-flex xs12 sm6 md4 lg3>
          <v-card
            text
            class="text-center ma-3"
            max-height="250"
            min-height="245"
            :hover="true"
            to="/collaborators/add"
          >
            <v-card-text class="center-content">
              <div class="green--text display-4">+</div>
            </v-card-text>
          </v-card>
        </v-flex>

        <v-flex xs12 sm6 md4 lg3 v-for="person in team" :key="person.name">
          <v-card
            text
            class="ma-3 text-center"
            max-height="250"
            min-height="245"
            :loading="false"
            :hover="true"
            :to="'/collaborators/' + person.id"
          >
            <v-responsive class="pt-4">
              <v-avatar size="100" class="grey lighten-2">
                <img src alt />
              </v-avatar>
            </v-responsive>

            <v-card-text>
              <div class="subheading">{{person.name}}</div>
              <div class="grey--text">{{person.role}}</div>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "collaborators",
  data() {
    return {
      team: [
        { id: "1", name: "Jorge", role: "Voluntario", avatar: "" },
        { id: "2", name: "Maria", role: "Doctor", avatar: "" },
        { id: "3", name: "Juan", role: "Odontólogo", avatar: "" },
        { id: "4", name: "Carmen", role: "Pastor", avatar: "" },
        { id: "5", name: "Miguel", role: "Nutricionista", avatar: "" }
      ]
    };
  }
};
</script>

<style scoped>
.center-content {
  padding-top:25%;
}
</style>