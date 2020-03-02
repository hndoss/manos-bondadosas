<template>
  <div>
    <h1>Collaborators</h1>

    <router-link tag="li" to="/collaborators/add">Add Collaborator</router-link>

    <h2>General List</h2>

    <v-row>
      <v-col cols="12" sm="5" offset-sm="3">
        <v-card>
          <v-container fluid>
            <v-row>
              <v-col class="d-flex child-flex" cols="7">
                <v-card flat tile class="d-flex">
                  <v-img
                    src="https://picsum.photos/500/300?image=1"
                    lazy-src="https://picsum.photos/10/6?image=1"
                    aspect-ratio="1"
                    class="grey lighten-2"
                  >
                    <template v-slot:placeholder>
                      <v-row class="fill-height ma-0" align="center" justify="center">
                        <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                      </v-row>
                    </template>
                  </v-img>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "collaborators"
};
</script>

<style scoped>
</style>