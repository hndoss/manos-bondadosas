<template>
  <div>
    <form>
      <v-col xs9 sm8 md8 lg8>
        <v-container>
          <v-text-field v-model="firstName" :counter="10" label="First Name" required></v-text-field>
          <v-text-field v-model="lastName" :counter="10" label="Last Name" required></v-text-field>
          <v-text-field v-model="age" :counter="10" label="Age" required></v-text-field>
          <v-text-field v-model="sex" :counter="10" label="Sex" required></v-text-field>
          <v-text-field v-model="email" :counter="10" label="Email" required></v-text-field>

          <!-- <v-text-field
            v-model="firstName"
            :counter="10"
            label="Last Name"
            required
            @input="$v.name.$touch()"
            @blur="$v.name.$touch()"
          ></v-text-field>Age - Combobox
          <v-radio-group :mandatory="true">
            <v-radio label="Male" value="M"></v-radio>
            <v-radio label="Feminine" value="F"></v-radio>
          </v-radio-group>

          <v-text-field
            v-model="email"
            label="E-mail"
            required
            @input="$v.email.$touch()"
            @blur="$v.email.$touch()"
          ></v-text-field>

          <v-text-field v-model="name" :counter="10" label="Age" required></v-text-field>
          <v-text-field v-model="name" :counter="10" label="Sex" required></v-text-field>-->
        </v-container>
      </v-col>

      <v-col xs3 sm4 md4 lg4>
        <v-container>
          <v-checkbox label="Do you agree?" required></v-checkbox>
        </v-container>
      </v-col>

      <v-btn class="mr-4" @click="submit">Submit</v-btn>
      <!-- <v-btn @click="clear">clear</v-btn> -->
    </form>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, maxLength, email } from "vuelidate/lib/validators";
import axios from "axios";

export default {  
  mixins: [validationMixin],
  name: "registerCollaborator",
  validations: {
    name: { required, maxLength: maxLength(10) },
    email: { required, email },
    select: { required },
    checkbox: {
      checked(val) {
        return val;
      }
    }
  },
  data: () => ({
    firstName: "",
    lastName: "",
    email: "",
    age: "",
    sex: ""
  }),

  methods: {
    clear() {
      this.$v.$reset();
      this.name = "";
      this.email = "";
      this.select = null;
      this.checkbox = false;
    },
    submit() {
      this.$v.$touch();
      console.log('send');
      let post = {
        first_name: this.firstName,
        last_name: this.lastName,
        email: this.email,
        age: this.age,
        sex: this.sex
      };
      axios
        .post("http://localhost:8000/api/v1/collaborators/", post)
        .then(result => {
          console.log(result);
        });
    }
  }
};
</script>

<style>
</style>