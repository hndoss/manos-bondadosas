<template>
  <div>
    <h1>Collaborators</h1>

    <div class="my-2">
      <v-btn>
        <router-link to="/collaborators/add">+</router-link>
      </v-btn>
    </div>
    <h2>General List</h2>

    <v-container class="my-5">

      <v-layout row wrap>
        <v-flex xs12 sm6 md4 lg3>
          <v-hover>
            <v-card
              text
              class="text-xs-center ma-3"
              slot-scope="{ hover }"
              :class="`elevation-${hover ? 20 : 2}`"
            >
              <v-card-text>
                <div class="grey--text">+</div>
              </v-card-text>
            </v-card>
          </v-hover>
        </v-flex>

        <v-flex xs12 sm6 md4 lg3 v-for="person in team" :key="person.name">
          <v-hover>
            <v-card
              text
              class="ma-3 text-xs-center"
              slot-scope="{ hover }"
              :class="`elevation-${hover ? 20 : 2}`"
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
          </v-hover>
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
        { name: "The Net Ninja", role: "Web developer" },
        { name: "Ryu", role: "Graphic designer" },
        { name: "Chun Li", role: "Web developer" },
        { name: "Gouken", role: "Social media" },
        { name: "Yoshi", role: "Sales guru" }
      ]
    };
  }
};
</script>

<style scoped>
</style>