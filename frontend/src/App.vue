<template>
  <v-app>
    <appBar />
    <sideBar xs3 sm4 md2 lg4 />

    <v-content xs9 sm8 md2 lg8>
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



// <container>
// <side-bar />
// <content>
// <router-view />
// </content>
// </container>
// container debe tener una clase que tenga la propiedad display:flex