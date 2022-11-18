<template>
  <div class="container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
    </div>

    <div class="content">
      <h1 class="is-size-1 title">{{ id }}</h1>
    </div>
    <!-- Button to submit -->
    <div class="field px-5">
      <div class="control has-text-centered">
        <button
          @click="acceptChallenge"
          class="button is-primary"
          type="button"
        >
          Submit
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { challengeStore } from "../stores/challengeStore";
import { userStore } from "../stores/userStore";
import axios from "axios";

export default {
  name: "SelectChallenge",
  setup() {
    const challenge_store = challengeStore();
    const user_store = userStore();
    return {
      challenge_store,
      user_store,
    };
  },
  mounted() {
    // get the challenge from the store by id
    this.challenge = this.challenge_store.challenges.find(
      // doesn't work for now
      (challenge) => challenge.id === this.$route.params.id
    );
  },
  data() {
    return {
      id: this.$route.params.id,
    };
  },
  methods: {
    goBack() {
      this.$router.push("/challenge"); // For the moment it will change the three challenges from the previous page
    },
    acceptChallenge() {
      // send the challenge to the backend
      axios
        .post("http://localhost:5000/accept_challenge", {
          challengeId: this.id,
          isAccepted: true,
        })
        .then((response) => {
          if (response.data.success) {
            this.user_store.userActiveChallenge = this.challenge;
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
</style>
