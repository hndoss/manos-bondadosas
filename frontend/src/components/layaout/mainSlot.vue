<template>
  <v-app id="inspire">
    <v-app-bar :clipped-left="$vuetify.breakpoint.lgAndUp" app color="primary" dark :src="bg">
      <v-toolbar-title style="width: 300px" class="ml-0">
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <span class="hidden-sm-and-down mx-2">Manos Bondadosas</span>
      </v-toolbar-title>

      <v-row class="flex-column">
        <v-form
          v-if="isGranted('ROLE_OTHER_SEARCH')"
          method="get"
          class="hidden-sm-and-down"
          @submit.prevent="search"
        >
          <v-text-field
            v-model="q"
            flat
            hide-details
            solo-inverted
            prepend-inner-icon="fas fa-search"
            label="Search"
          ></v-text-field>
        </v-form>
      </v-row>

      <v-spacer></v-spacer>

      <span class="mx-2">{{ username }}</span>
      <v-btn icon @click="signOut">
        <v-icon>mdi-power</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      :clipped="$vuetify.breakpoint.lgAndUp"
      app
      dark
      hide-overlay
      :src="bg"
    >
      <v-list dense>
        <template v-for="item in items">
          <v-list-group
            v-if="isGrantedItem(item)"
            :key="item.label"
            ref="listGroup"
            v-model="item.model"
            :prepend-icon="prependIcon(item)"
            :append-icon="appendIcon(item)"
            @click="listItemClick(item)"
          >
            <template v-slot:activator>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>{{ item.label }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>

            <template v-for="(child, i) in item.children">
              <v-list-item
                v-if="isGrantedItem(child)"
                :key="i"
                :class="{
                  'active-item': routeName(child.route) === activeRoute
                }"
                @click="listItemClick(child)"
              >
                <v-list-item-action v-if="child.icon">
                  <v-icon right>{{ child.icon }}</v-icon>
                </v-list-item-action>

                <v-list-item-content>
                  <v-list-item-title>{{ child.label }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-list-group>
        </template>
      </v-list>
    </v-navigation-drawer>

    <v-content>
      <router-view />
    </v-content>

    <footer></footer>
    <!--

    <modal-not-done-tasks
      :tasks="tasks"
      :dialog="dialog"
      @dialog-close="dialog = false"
    ></modal-not-done-tasks>-->
  </v-app>
</template>

<script>
import fecha from "fecha";
import bg from "@/assets/bg.png";
// import ModalNotDoneTasks from './ModalNotDoneTasks'
// import axios from '../../interceptor'
import Footer from "@/components/layaout/footer"
import axios from "axios";

export default {
  name: "MainSlot",
  components: { Footer },
  // components: { ModalNotDoneTasks },
  data() {
    return {
      bg,
      fecha,
      q: null,
      tasks: [],
      dialog: false,
      drawer: null,
      activeRoute: null,
      items: [
        {
          label: "Dashboard",
          icon: "fas fa-home",
          route: "Dashboard",
          role: "ROLE_USER_DASHBOARD"
        },
        {
          label: "Calendar",
          icon: "far fa-calendar-alt",
          route: "Calendar",
          role: "ROLE_OTHER_CALENDAR"
        },
        {
          label: "People",
          icon: "fas fa-users",
          children: [
            {
              label: "Collaborators",
              icon: "fas fa-users",
              route: "ListCollaborators",
              role: "ROLE_DOCUMENT_LIST"
            },
            {
              label: "Beneficiaries",
              icon: "fas fa-users",
              route: "ListBeneficiaries",
              role: "ROLE_TEMPLATE_LIST"
            }
          ],
          role: "ROLE_CLIENT_LIST"
        },
        {
          label: "Projects",
          icon: "fas fa-hammer",
          route: "ListProjects",
          role: "ROLE_COMPANY_LIST"
        },
        {
          label: "Places",
          icon: "fas fa-building",
          children: [
            {
              label: "Regions",
              icon: "fas fa-map-marked",
              route: "fas fa-building",
              role: "ROLE_CONTACT_LIST"
            },
            {
              label: "Locals",
              icon: "fas fa-building",
              route: "AddressList",
              role: "ROLE_ADDRESS_LIST"
            }
          ]
        },
        {
          label: "Inventories",
          icon: "fas fa-box",
          children: [
            {
              label: "category",
              icon: "format_align_justify",
              route: "CategoryList",
              role: "ROLE_CATEGORY_LIST"
            },
            {
              label: "product",
              icon: "format_align_justify",
              route: "ProductList",
              role: "ROLE_PRODUCT_LIST"
            }
          ]
        },
        {
          label: "Reports",
          icon: "fas fa-chart-pie",
          route: "reports",
          role: "ROLE_USER_DASHBOARD"
        },
      ]
    };
  },
  computed: {
    username() {
      // return this.$store.getters['auth/jwtDecoded'].name
      return "Admin";
    }
  },
  watch: {
    $route(to, from) {
      this.activeRoute = this.routeName(to.name)
      this.initActiveMenuItem()
    }
  },
  created() {
    this.activeRoute = this.routeName(this.$route.name);
  },
  mounted() {
    if (this.isGranted("ROLE_TASK_LIST")) {
      // this.getTasks()
    }

    this.initActiveMenuItem();
  },
  methods: {
    initActiveMenuItem() {
      this.items.forEach(i => {
        if (i.children && i.children.length) {
          i.children.forEach(el => {
            if (this.routeName(el.route) === this.activeRoute) {
              i.model = true;
            }
          });
        } else if (this.routeName(i.route) === this.activeRoute) {
          i.model = true;
        }
      });
    },
    routeName(route) {
      return route ? route.replace(/(List|Show|Create|Update)/, "") : "";
    },
    prependIcon(item) {
      if (item.icon) {
        return item.icon;
      }
    },
    appendIcon(item) {
      if (item.children && item.children.length) {
        return "fas fa-arrow-circle-down";
      }

      return null;
    },
    listItemClick(item) {
      if (item.route) {
        this.$router.push({ name: item.route });
      }
    },
    isGranted(item) {
      return true;
    },
    isGrantedItem(item) {
      if (item.role) {
        return this.isGranted(item.role);
      }

      if (item.children) {
        return item.children.some(child => this.isGranted(child.role));
      }

      return false;
    },
    search() {
      this.$router.push({ name: "Search", query: { q: this.q } });
    },
    signOut() {
      this.$store.dispatch("auth/logout");
    },
    getTasks() {
      const url = `${process.env.VUE_APP_API_URL}/tasks/deadline`;

      axios.get(url).then(response => {
        this.tasks = response.data["hydra:member"];

        if (this.tasks.length) {
          this.dialog = true;
        }
      });
    }
  }
};
</script>

<style lang="scss">
.v-navigation-drawer {
  .v-list {
    &-group--active {
      .v-list-group__items {
        background: #142430;
      }
      .v-list-group__header {
        background: #142430;
      }
    }
    .theme--dark {
      .v-icon {
        color: #fff !important;
      }
    }
  }
}
.active-item {
  position: relative;
  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0.3 !important;
    background-color: #fafafa !important;
  }
}
</style>