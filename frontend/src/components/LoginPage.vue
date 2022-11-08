<template>
  <div class="login-page is-fullheight">
    <div class="columns is-mobile is-centered">
      <div class="column is-6">
        <img src="../assets/set_1/1.png" alt="Eco-Eco Logo" width="275" />
      </div>
    </div>

    <h1 class="title is-1 has-text-centered">Login</h1>
    <p class="subtitle has-text-centered is-3">Please login to continue</p>
    <form @submit.prevent="login">
      <div class="field">
        <label class="label">Username</label>
        <div class="control">
          <input
            class="input"
            type="text"
            placeholder="Username"
            v-model="username"
          />
        </div>
      </div>
      <div class="field">
        <label class="label">Password</label>
        <div class="control">
          <input
            class="input"
            type="password"
            placeholder="Password"
            v-model="password"
          />
        </div>
      </div>
      <div class="field">
        <div class="control">
          <button class="button is-primary">Login</button>
        </div>
      </div>
    </form>
    <img class="is-image" src="../assets/set_1/divider.png" />
    <p class="subtitle has-text-centered is-3">Don't have an account yet ?</p>
    <router-link to="/register" class="button is-primary">
      Register
    </router-link>
    <img class="is-image" src="../assets/set_1/8.png" />
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login() {
      this.$store.dispatch("login", {
        username: this.username,
        password: this.password,
      });
    },
  },
};
</script>

<style>
.login-page {
  background-image: url("../assets/set_1/login_background.png");
}
</style>
