<template>
  <div class="container">
    <!-- Header with user name -->
    <div class="content mx-5 mb-5 pt-5">
      <h1 class="is-title is-size-1">Hi, {{ userName }}!</h1>
      <h2 class="is-subtitle is-size-3">Let's get to know you better ...</h2>
    </div>

    <!-- Bubble with question -->
    <div id="gradient-text" class="content mx-5 mb-5 py-5">
      <p class="is-size-4 px-5">What modes of travel do you have access to ?</p>
    </div>

    <!-- Form with multiselect -->
    <form class="field is-grouped is-grouped-multiline mx-5 my-6">
      <div
          v-for="(mean, index) in possibleMeansOfTransport"
          :key="index"
          class="control"
      >
        <a
            @click="toggleSelect(mean)"
            class="button is-rounded"
            :class="{ 'is-info': isActive(mean) }"
        >{{ sentenceCase(mean) }}</a
        >
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
import {userStore} from "../stores/userStore";

export default {
  name: "QuestionnairePage",
  setup() {
    const store = userStore();
    return {
      store,
    };
  },
  data() {
    return {
      userName: this.store.userName,
      possibleMeansOfTransport: [
        "Walking",
        "Busses",
        "Car",
        "Subway",
        "Bike",
        "Subway",
        "Trains"
      ],
      selectedMeansOfTransport: [],
    };
  },
  methods: {
    toggleSelect(mean) {
      if (this.selectedMeansOfTransport.includes(mean)) {
        this.selectedMeansOfTransport = this.selectedMeansOfTransport.filter(
            (item) => item !== mean
        );
      } else {
        this.selectedMeansOfTransport.push(mean);
      }
      console.log(this.selectedMeansOfTransport);
    },
    sentenceCase(word) {
      let text = word
          .split(". ")
          .map((e) => e.charAt(0).toUpperCase() + e.substring(1).toLowerCase())
          .join(". ");
      return text;
    },
    isActive(mean) {
      return this.selectedMeansOfTransport.includes(mean);
    },
    submit() {
      axios
          .post("http://localhost:5000/api/questionnaire_1", {
            userId: this.store.userId,
            userName: this.store.userName,
            meansOfTransport: this.selectedMeansOfTransport, // unoreded list of selected means of transport
          })
          .then((response) => {
            if (response.data.status === "success") {
              // what to do if the request is not a success ? (probably display an error message)
              this.store.userMeansOfTransport = this.selectedMeansOfTransport;
              this.$router.push("/questionnaire_2");
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
@import url("https://fonts.googleapis.com/css2?family=Dancing+Script:wght@500&display=swap");

.is-title {
  font-family: "Dancing Script", cursive;
}

.container {
  height: 100vh;
  background-image: url("../assets/set_1/login_background.png");
}

.content h1,
h2 {
  color: rgb(12, 50, 110);
}

#gradient-text {
  border-radius: 35px;
  color: rgb(12, 50, 110);
  font-weight: 500;
  background-color: #a6dbf2;
}
</style>
