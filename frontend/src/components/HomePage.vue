<template>
  <div class="main-container content">
    <h1 class="title is-1 has-text-centered">Eco-Eco</h1>
    <div class="content columns"></div>
    <MenuBar />
  </div>
</template>

<script>
// import MenuBar component
import MenuBar from "./MenuBar.vue";

export default {
  name: "HomePage",
  components: {
    MenuBar,
  },
};
</script>

<style>
.main-container {
  background-image: url("../assets/set_1/login_background.png");
}
</style>
