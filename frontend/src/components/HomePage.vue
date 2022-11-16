<template>
  <div class="main-container is-fullheight container">
    <h1 class="title is-1 has-text-centered">Eco-Eco</h1>
    <MenuBar @toggle-modal="changeModal" />
    <NotImplemented @toggle-modal="changeModal" :isActive="isActive" />
  </div>
</template>

<script>
// import MenuBar component
import MenuBar from "./MenuBar.vue";
import NotImplemented from "./NotImplemented.vue";

export default {
  name: "HomePage",
  components: {
    MenuBar,
    NotImplemented,
  },
  data() {
    return {
      isActive: false,
    };
  },
  methods: {
    changeModal() {
      // change the value of isActive
      console.log("change modal");
      this.isActive = !this.isActive;
    },
  },
};
</script>

<style>
.main-container {
  background-image: url("../assets/set_1/login_background.png");
  height: 100vh;
}
</style>
