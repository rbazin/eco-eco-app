<template>
  <div class="container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
    </div>

    <!-- Bubble with question -->
    <div id="gradient-text" class="content mx-5 mb-5 py-5">
      <p class="is-size-4 px-5">How frequently do you visit these places ?</p>
    </div>

    <!-- Form with radio select -->
    <form class="field is-grouped is-grouped-multiline mx-5 my-6">
      <div
        v-for="(place, index) in possiblePlaces"
        :key="index"
        class="control"
      >
        <label class="radio">
            <input type="radio" name="answer" value="never" v-model="selectedPlace">
            
        </label>
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
