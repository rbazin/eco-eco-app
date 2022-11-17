<template>
  <div class="container">
    <!-- Back button -->
    <div @click="goBack">
      <font-awesome-icon icon="fa-solid fa-arrow-left" />
    </div>

    <!-- Bubble with question -->
    <div id="gradient-text" class="content mx-5 mb-5 py-5">
      <p class="is-size-4 px-5">How frequently do you visit these places ?</p>
    </div>
  </div>
</template>
<script>
import { userStore } from "../stores/userStore";

export default {
  name: "QuestionnairePage2",
  setup() {
    const store = userStore();
    return {
      store,
    };
  },
  methods: {
    goBack() {
      this.$router.push("/questionnaire_1");
    },
  },
};
</script>
<style scoped>
.container {
  height: 100vh;
  background-image: url("../assets/set_1/login_background.png");
}
#gradient-text {
  border-radius: 35px;
  color: rgb(12, 50, 110);
  font-weight: 500;
  background-color: #a6dbf2;
}
</style>
