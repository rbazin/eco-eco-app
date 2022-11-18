<template>
  <div class="container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
    </div>

    <!-- Challenges -->
    <div
      v-for="(challenge, index) in challenges"
      :key="index"
      class="content mx-5 mb-5 py-5 challenge"
      @click="goToChallenge(challenge)"
    >
      <p class="is-size-4 px-5 has-text-centered">{{ challenge.title }}</p>
    </div>

    <!-- Button to see full list -->
    <div class="field mt-6 px-5">
      <div class="control has-text-centered">
        <button @click="goToFullList" class="button is-info" type="button">
          See full list
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { userStore } from "../stores/userStore";
import { challengeStore } from "../stores/challengeStore";

export default {
  name: "ChallengePage",
  setup() {
    const user_store = userStore();
    const challenge_store = challengeStore();
    return {
      user_store,
      challenge_store,
    };
  },
  data() {
    return {
      challenges: [
        {
          id: 1,
          title: "Challenge 1",
          fact: "lorem ipsum",
        },
        {
          id: 2,
          title: "Challenge 2",
          fact: "lorem ipsum",
        },
        {
          id: 3,
          title: "Challenge 3",
          fact: "lorem ipsum",
        },
      ],
    };
  },
  methods: {
    goToChallenge(challenge) {
      this.$router.push({
        name: "SelectChallenge",
        path: "/challenge",
        params: {
          id: challenge.id,
        },
      });
    },
    goBack() {
      this.$router.push("/home");
    },
    goToFullList() {
      this.$router.push("/all-challenges");
    },
    // Function to get the challenge from the backend
    getChallenges() {
      // Get 3 challenges from the backend, each challenge should be an object {id, title, fact, reward}

      // check if there are challenges in the store before asking backend
      //if (this.challenge_store.getChallenges().length > 0) {
      //  return this.challenge_store.getChallenges();
      //}
      axios
        .get("http://localhost:5000/api/challenges", {
          params: {
            userId: this.store.userId, // the get request sends the id of the user to personalize the challenges sent
          },
        })
        .then((response) => {
          console.log(response);
          if (response.data.success) {
            this.challenges = response.data.challenges;
            this.challenge_store.setChallenges(this.challenges);
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
  background-image: url("../assets/set_1/login_background.png");
  height: 100vh;
}
.challenge {
  color: rgb(12, 50, 110);
  background-color: #ffffff;
  border-radius: 35px;
}
</style>
