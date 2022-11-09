<template>
  <div class="login-page is-fullheight">
    <figure class="content has-text-centered mb-0">
      <img src="../assets/set_1/1.png" alt="Eco-Eco Logo" width="200" />
    </figure>

    <h1 class="title is-1 has-text-centered">Login</h1>
    <p class="subtitle has-text-centered is-3">Please login to continue</p>
    <form @submit.prevent="login">
      <div class="field columns is-mobile px-5">
        <figure class="column is-3 has-text-centered">
          <img
            src="../assets/set_1/u.png"
            alt="User login icon"
            class="image is-48x48"
          />
        </figure>
        <div class="control column">
          <input
            class="input"
            type="text"
            placeholder="Username"
            v-model="username"
          />
        </div>
      </div>
      <div class="field columns is-mobile px-5">
        <figure class="column is-3 has-text-centered">
          <img
            src="../assets/set_1/9.png"
            alt="User login icon"
            class="image is-48x48"
          />
        </figure>
        <div class="control column">
          <input
            class="input"
            type="password"
            placeholder="Password"
            v-model="password"
          />
        </div>
      </div>
      <div class="field">
        <div class="control has-text-centered">
          <button class="button is-primary">Login</button>
        </div>
      </div>
    </form>
    <img class="is-image" src="../assets/set_1/divider.png" />
    <p class="subtitle has-text-centered is-4">Don't have an account yet ?</p>
    <div class="has-text-centered">
      <router-link to="/register" class="button is-primary">
        Register
      </router-link>
    </div>
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
    login() {},
  },
};
</script>

<style>
.login-page {
  background-image: url("../assets/set_1/login_background.png");
}
</style>
