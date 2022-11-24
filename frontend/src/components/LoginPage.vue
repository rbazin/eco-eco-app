<template>
  <div class="login-page is-fullheight container">
    <figure class="content has-text-centered mb-0">
      <img src="../assets/set_1/1.png" alt="Eco-Eco Logo" width="200" />
    </figure>

    <h1 class="title is-1 has-text-centered">Login</h1>
    <p class="subtitle has-text-centered is-3">Please login to continue</p>
    <form @submit.prevent="login">
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
            :class="{ 'is-danger': !isUsernameValid }"
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
            :class="{ 'is-danger': !isUsernameValid }"
            type="password"
            placeholder="Password"
            v-model="password"
          />
        </div>
        <p
          v-if="!isUsernameValid"
          class="help has-text-centered is-size-5 has-text-danger"
          :class="{ 'is-danger': !isUsernameValid }"
        >
          User doesn't exist, please register first
        </p>
      </div>
      <div class="field">
        <div class="control has-text-centered">
          <button @click="Login" class="button is-primary">Login</button>
        </div>
      </div>
    </form>
    <img class="is-image" src="../assets/set_1/divider.png" />
    <p class="subtitle has-text-centered is-4">Don't have an account yet ?</p>
    <div class="has-text-centered">
      <router-link to="/register" class="button is-primary"> Register </router-link>
    </div>
    <img class="is-image" src="../assets/set_1/8.png" />
  </div>
</template>

<script>
import axios from "axios";
import { userStore } from "../stores/userStore.js";

export default {
  name: "LoginPage",
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
      isUsernameValid: true,
    };
  },
  methods: {
    // Login function with axios
    Login() {
      axios
        .post("http://localhost:5000/api/login", {
          // call to the backend
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          console.log(response);
          if (response.data.status === "success") {
            // Stores data about the user that will be needed everywhere in the user store
            this.store.userId = response.data.userId;
            this.store.userName = response.data.userName;
            this.store.userDroplets = response.data.userDroplets;
            this.store.userStreak = response.data.userStreak;
            this.store.userLoggedIn = true;
            this.$router.push("/home"); // Redirect to home page after login
          } else {
            this.isUsernameValid = false;
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
.login-page {
  background-image: url("../assets/set_1/login_background.png");
  min-height: 100vh;
  background-repeat: repeat-y;
}
</style>
