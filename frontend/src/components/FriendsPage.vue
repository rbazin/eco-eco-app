<template>
  <div class="container main-container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
    </div>

    <h1 class="title is-1 has-text-centered">Friends</h1>
    
    <FriendComponent />
  </div>
</template>
<script>
import FriendComponent  from "./FriendComponent.vue"

export default {
  name: "App",
  components : {
    FriendComponent,
  },
  methods: {
    goBack() {
      this.$router.push("/home");
    },
  }
};
</script>
<style scoped>
.title {
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  top: -50px;
}
.container {
  min-height: 100vh;
  background-image: url("../assets/set_1/login_background.png");
  background-repeat: repeat-y;
}
</style>
