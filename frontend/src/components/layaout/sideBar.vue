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
    absolute
    dark
  >
    <v-list dense nav class="py-0">
      <v-divider></v-divider>

      <v-list-item v-for="item in items" :key="item.title" link>
        <router-link class="menu-item" :to="{ path: item.link }">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </router-link>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "sideBar",
  data() {
    return {
      drawer: true,
      items: [
        { title: "Dashboard", icon: "mdi-view-dashboard", link: "/" },
        { title: "Collaborators", icon: "mdi-image", link: "/collaborators" },
        { title: "Benefited", icon: "mdi-image", link: "/benefited" },
        { title: "Events", icon: "mdi-help-box", link: "/events" },
        { title: "Admin", icon: "mdi-help-box", link: "/admin" },
      ],
      right: false,
      miniVariant: false,
      expandOnHover: false,
      background: false,
      bottom: false,
      clipped: true,
      height: "100%"
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
.menu-item {
  text-decoration: none;
  color: white;
  display: flex;
}
</style>