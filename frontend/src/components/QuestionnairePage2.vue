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
    <form
      v-for="(transport, index) in frequenciesOfPlaces"
      :key="index"
      class="field is-grouped is-grouped-multiline mx-6"
    >
      <div class="pb-4">
        <label class="label">{{ sentenceCase(transport.mean) }}</label>
        <div class="control">
          <label class="radio">
            <input type="radio" value="daily" v-model="transport.frequency" />
            Daily
          </label>
          <label class="radio">
            <input type="radio" value="weekly" v-model="transport.frequency" />
            Weekly
          </label>
          <label class="radio">
            <input type="radio" value="monthly" v-model="transport.frequency" />
            Monthly
          </label>
        </div>
      </div>
    </form>

    <!-- Button to submit -->
    <div class="field px-5">
      <div class="control has-text-centered">
        <button @click="submit" class="button is-primary" type="submit">
          Submit
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { userStore } from "../stores/userStore";

export default {
  name: "QuestionnairePage2",
  setup() {
    const store = userStore();
    return {
      store,
    };
  },
  data() {
    return {
      // Later we'll call the backend to know the possible places
      frequenciesOfPlaces: [
        { mean: "work", frequency: null },
        { mean: "school", frequency: null },
        { mean: "gym", frequency: null },
        { mean: "theater", frequency: null },
        { mean: "groceries", frequency: null },
      ],
    };
  },
  methods: {
    goBack() {
      this.$router.push("/questionnaire_1");
    },
    sentenceCase(word) {
      let text = word
        .split(". ")
        .map((e) => e.charAt(0).toUpperCase() + e.substring(1).toLowerCase())
        .join(". ");
      return text;
    },
    submit() {
      // Send means of Transport to backend
      console.log(this.frequenciesOfPlaces);
      axios
        .post("http://localhost:5000/api/questionnaire_2", {
          userId: this.store.userId,
          userName: this.store.userName,
          frequenciesOfPlaces: this.frequenciesOfPlaces, // unoreded list of means of transport object, eg: {mean: "Busses", frequency: "daily"}
        })
        .then((response) => {
          if (response.data.status === "success") {
            this.store.userFrequenciesOfTransport = this.frequenciesOfPlaces;
            this.$router.push("/home");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>
.container {
  height: 100vh;
  background-image: url("../assets/set_1/login_background.png");
}
.label {
  color: rgb(12, 50, 110);
}
#gradient-text {
  border-radius: 35px;
  color: rgb(12, 50, 110);
  font-weight: 500;
  background-color: #a6dbf2;
}
</style>
