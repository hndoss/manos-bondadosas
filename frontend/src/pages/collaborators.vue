<template>
  <div>
    <h1>Collaborators</h1>SEARCH BAR
    <v-container class="my-5">
      <v-layout row wrap>
        <v-flex xs12 sm6 md4 lg3>
          <v-card
            text
            class="text-xs-center ma-3"
            max-height="800"
            min-height="200"
            :hover="true"
            to="/collaborators/add"
          >
            <v-card-text class="text-center">
              <div class="green--text display-4">+</div>
            </v-card-text>
          </v-card>
        </v-flex>

        <v-flex xs12 sm6 md4 lg3 v-for="person in team" :key="person.name">
          <v-card
            text
            class="ma-3 text-xs-center"
            max-height="800"
            min-height="200"
            :loading="false"
            :hover="true"
            :to="'/collaborators/' + person.id"
          >
            <v-responsive class="pt-4">image goes here.</v-responsive>

            <v-card-text>
              <div class="subheading">{{person.name}}</div>
              <div class="grey--text">{{person.role}}</div>
            </v-card-text>

            <v-card-actions>
              <v-btn text color="grey" icon>
                <v-icon small left>message-text</v-icon>
              </v-btn>
              <span>Message</span>
            </v-card-actions>
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
        { id: "1", name: "The Net Ninja", role: "Web developer" },
        { id: "2", name: "Ryu", role: "Graphic designer" },
        { id: "3", name: "Chun Li", role: "Web developer" },
        { id: "4", name: "Gouken", role: "Social media" },
        { id: "5", name: "Yoshi", role: "Sales guru" }
      ]
    };
  }
};
</script>

<style scoped>
</style>