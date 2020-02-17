<template>
  <v-app>
    <sideBar />

    <appBar />

    <v-content>
      <router-view />
    </v-content>

    <footerBar />
  </v-app>
</template>

<script>
import sideBar from "@/components/layaout/sideBar";
import appBar from "@/components/layaout/appBar";
import footerBar from "@/components/layaout/footerBar";

export default {
  name: "App",

  components: {
    sideBar,
    appBar,
    footerBar
  },

  data: () => ({})
};
</script>