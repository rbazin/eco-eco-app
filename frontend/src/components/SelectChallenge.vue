<template>
  <div class="container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
    </div>
    <h1 class="is-size-1 title">{{ id }}</h1>
  </div>
</template>

<script>
export default {
  name: "SelectChallenge",
  data() {
    return {
      id: this.$route.params.id,
    };
  },
  methods: {
    goBack() {
      this.$router.push("/challenge"); // For the moment it will change the three challenges from the previous page
    },
  },
};
</script>

<style scoped>
.container {
  height: 100vh;
  background-image: url("../assets/set_1/login_background.png");
}
</style>
