<template>
  <v-card color="blue-grey darken-1" dark :loading="isUpdating">
    <template v-slot:progress>
      <v-progress-linear absolute color="green lighten-3" height="4" indeterminate></v-progress-linear>
    </template>
    <v-img height="200" :src="require(`@/assets/${background}`)" />

    <v-form>
      <v-container>
        <v-row>
          <v-col cols="12">
            <p>{{ instruction }}</p>

            <v-autocomplete
              v-model="friends"
              :disabled="isUpdating"
              :items="this.collection"
              filled
              chips
              color="blue-grey lighten-2"
              label="Select"
              item-text="first_name"
              item-value="first_name"
              multiple
            >
              <template v-slot:selection="data">
                <v-chip
                  v-bind="data.attrs"
                  :input-value="data.selected"
                  close
                  @click="data.select"
                  @click:close="remove(data.item)"
                >
                  <v-avatar left>
                    <v-img :src="data.item.avatar"></v-img>
                  </v-avatar>
                  {{ data.item.first_name }}
                </v-chip>
              </template>
              <template v-slot:item="data">
                <template v-if="typeof data.item !== 'object'">
                  <v-list-item-content v-text="data.item"></v-list-item-content>
                </template>
                <template v-else>
                  <v-list-item-avatar>
                    <img :src="data.item.avatar" />
                  </v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-title v-html="data.item.first_name"></v-list-item-title>
                  </v-list-item-content>
                </template>
              </template>
            </v-autocomplete>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
    <v-divider></v-divider>
    <v-card-actions>
      <v-btn :loading="isUpdating" color="blue-grey darken-3" depressed @click="isUpdating = true">
        <v-icon left>mdi-update</v-icon>Save
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Card",
  props: ["background", "instruction", "collection"],
  data () {
    return {
        friends: [],
        isUpdating: false,
        name: 'Midnight Crew',
        title: 'The summer breeze',
    }
  },
  watch: {
    isUpdating (val) {
      if (val) {
        setTimeout(() => (this.isUpdating = false), 1000)
      }
    },
  },
  methods: {
    remove (item) {
      const index = this.friends.indexOf(item.name)
      if (index >= 0) this.friends.splice(index, 1)
    },
  },
}
</script>

<style>
</style>