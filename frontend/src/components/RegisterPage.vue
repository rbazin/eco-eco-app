<template>
  <div class="login-page is-fullheight container">
    <figure class="content has-text-centered mb-0">
      <img src="../assets/set_1/1.png" alt="Eco-Eco Logo" width="200" />
    </figure>

    <h1 class="title is-1 has-text-centered">Register</h1>
    <p class="subtitle has-text-centered is-3">Please register to continue</p>
    <form @submit.prevent="register">
      <div class="field px-5">
        <div class="control is-vcentered columns is-mobile">
          <figure class="column is-offset-2 is-narrow">
            <img
              src="../assets/set_1/u.png"
              alt="User login icon"
              class="image is-48x48"
            />
          </figure>
          <input
            class="input column is-6"
            type="text"
            placeholder="Username"
            v-model="username"
          />
        </div>
      </div>
      <div class="field px-5">
        <div class="control mb-5 is-vcentered columns is-mobile">
          <figure class="column is-offset-2 is-narrow">
            <img
              src="../assets/set_1/9.png"
              alt="User login icon"
              class="image is-48x48"
            />
          </figure>
          <input
            class="input column is-6"
            type="password"
            placeholder="Password"
            v-model="password"
          />
        </div>
      </div>
      <div class="field px-5">
        <div class="control mb-5 is-vcentered columns is-mobile">
          <figure class="column is-offset-2 is-narrow">
            <img
              src="../assets/set_1/9.png"
              alt="User login icon"
              class="image is-48x48"
            />
          </figure>
          <input
            class="input column is-6"
            type="password"
            placeholder="Confirm password"
            v-model="confirmPassword"
          />
        </div>
      </div>
      <div class="field">
        <div class="control has-text-centered">
          <button @click="this.register()" class="button is-primary">
            Register
          </button>
        </div>
      </div>
    </form>
    <img class="is-image" src="../assets/set_1/divider.png" />
    <img class="is-image" src="../assets/set_1/8.png" />
  </div>
</template>
<script>
import axios from "axios";
import { userStore } from "../stores/userStore";

export default {
  name: "RegisterPage",
  setup() {
    const store = userStore();
    return {
      store,
    };
  },
  data() {
    return {
      username: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    register() {
      if (this.password !== this.confirmPassword) {
        alert("Passwords do not match");
        return;
      }
      axios
        .post("http://localhost:5000/api/signup", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          if (response.data.success) {
            // Backend has to reply if the registration was successful
            this.store.login(
              // If it was, we log the user in
              response.data.userId,
              response.data.userDroplets,
              response.data.userStreak
            );
            this.$router.push("/questionnaire_1");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style>
.register-page {
  background-image: url("../assets/set_1/login_background.png");
}
</style>
