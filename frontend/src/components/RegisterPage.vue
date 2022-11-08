<template>
  <div class="register-page">
    <div class="columns is-mobile is-centered">
      <div class="column is-6">
        <img src="../assets/set_1/1.png" alt="Eco-Eco Logo" />
      </div>
    </div>

    <h1 class="title is-1 has-text-centered">Register</h1>
    <p class="subtitle has-text-centered is-3">
      Please enter your details to continue
    </p>
    <form @submit.prevent="register">
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
        <label class="label">Confirm password</label>
        <div class="control">
          <input
            class="input"
            type="password"
            placeholder="Confirm password"
            v-model="confirmPassword"
          />
        </div>
      </div>
      <div class="field">
        <div class="control is-right">
          <button class="button is-primary">Register</button>
        </div>
      </div>
    </form>
    <img class="is-image" src="../assets/set_1/8.png" />
  </div>
</template>
<script>
export default {
  name: "RegisterPage",
  data() {
    return {
      username: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    register() {
      this.$store.dispatch("register", {
        username: this.username,
        password: this.password,
        confirmPassword: this.confirmPassword,
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
