<template>
  <div class="welcome-page content">
    <!-- Just a simple test page, for now it's the landing page -->
    <h1 class="title is-1">Welcome to the Eco-Eco App</h1>
    <p class="subtitle is-3">This is the welcome page</p>
    <div class="columns">
      <router-link to="/login" class="button is-primary column"
        >Login</router-link
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "WelcomePage",
};
</script>
<style></style>
