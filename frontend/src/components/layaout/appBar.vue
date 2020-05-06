<template>
  <div>
    <!-- <nav>
      <v-toolbar text app>
        <v-toolbar-title class="text-uppercae grey--text">
          <span class="font-weight-light">Todo</span>
          <span>Ninja</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn text color="grey"> </v-btn>
      </v-toolbar>
    </nav> -->
    <v-app-bar app >
      <div>this is the app bar</div>
    </v-app-bar>

    <!-- <v-navigation-drawer v-model="drawer" app class="indigo">
      <p>test</p>
    </v-navigation-drawer> -->
  </div>
</template>

<script>
export default {
  name: "appBar",
  data() {
    return {
      drawer: true
    };
  }
};
</script>

<style scoped>
</style>