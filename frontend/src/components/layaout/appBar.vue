<template>
  <v-app-bar app :clipped-left="clippedLeft" :dark="dark">
    <div>this is the app bar</div>
  </v-app-bar>
</template>

<script>
export default {
  name: "appBar",
  data() {
    return {
      clippedLeft: true,
      dark: true
    };
  }
};
</script>

<style scoped>
</style>