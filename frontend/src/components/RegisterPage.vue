<template>
  <div class="register-page is-fullheight container">
    <!-- Back button -->
    <div id="go-back" @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
    </div>

    <figure class="content has-text-centered mb-0">
      <img src="../assets/set_1/1.png" alt="Eco-Eco Logo" width="200" />
    </figure>

    <h1 class="title is-1 has-text-centered">Register</h1>
    <p class="subtitle has-text-centered is-3">Please register to continue</p>
    <form>
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
            :class="{ 'is-danger': !isValid }"
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
            :class="{ 'is-danger': !isValid }"
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
            :class="{ 'is-danger': !isValid }"
            v-model="confirmPassword"
          />
        </div>
        <p
          v-if="!isValid"
          class="help has-text-centered is-size-5 has-text-danger"
          :class="{ 'is-danger': !isValid }"
        >
          Username or Password already exist, please enter valid credentials
        </p>
      </div>
      <div class="field">
        <div class="control has-text-centered">
          <button @click="register" type="button" class="button is-primary">
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
      isValid: true,
    };
  },
  methods: {
    goBack() {
      this.$router.push("/login");
    },
    register() {
      console.log("Registering...");
      axios
        .post("http://localhost:5000/api/signup", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          console.log(response);
          if (response.data.success) {
            // Backend has to reply if the registration was successful
            this.store.userId = response.data.userId;
            this.store.userName = response.data.userName;
            this.store.userDroplets = response.data.userDroplets;
            this.store.userStreak = response.data.userStreak;
            this.store.userLoggedIn = true;
            this.$router.push("/questionnaire_1");
          } else {
            this.isValid = false;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>
.register-page {
  background-image: url("../assets/set_1/login_background.png");
  min-height: 100vh;
  background-size: cover;
  background-repeat: repeat-y;
}
#go-back {
  position: absolute;
  left: 0;
}
</style>
