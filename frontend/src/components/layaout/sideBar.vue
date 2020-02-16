<template>
  <v-navigation-drawer
    app
    v-model="drawer"
    :expand-on-hover="expandOnHover"
    :mini-variant="miniVariant"
    :right="right"
    :src="bg"
    :bottom="bottom"
    :clipped="clipped"
    :height="height"
    :width="width"
    absolute
    dark
  >
    <v-list dense nav class="py-0">
      <v-divider></v-divider>

      <v-list-item v-for="item in items" :key="item.title" link>
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'sideBar',
  data() {
    return {
      drawer: true,
      items: [
        { title: "Dashboard", icon: "mdi-view-dashboard" },
        { title: "People", icon: "mdi-image" },
        { title: "Events", icon: "mdi-help-box" },
        { title: "Admin", icon: "mdi-help-box" },
        { title: "About", icon: "mdi-help-box" }
      ],
      right: false,
      miniVariant: false,
      expandOnHover: false,
      background: false,
      bottom: true,
      clipped: true,
      height: "100%",
      width: "10%"
    };
  },
  computed: {
    bg() {
      return this.background
        ? "https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg"
        : undefined;
    }
  }
};
</script>

<style scoped>
</style>