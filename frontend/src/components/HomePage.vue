<template>
  <div class="main-container">
    <h1 class="title is-1 has-text-centered">Eco-Eco</h1>
    <MenuBar />
  </div>
</template>

<script>
import MenuBar from "./MenuBar.vue";

export default {
  name: "Home",
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
