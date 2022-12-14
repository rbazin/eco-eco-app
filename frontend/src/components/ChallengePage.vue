<template>
  <div class="container" id="challenges-container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
    </div>

    <h1 id="challenges-title" class="title is-1 has-text-centered">Challenges</h1>

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
    <div class="content is-centered has-text-centered pt-6">
      <div @click="goToFullList" class="button is-size-4 is-rounded is-info has-text-centered">
        See full list
      </div>
    </div>

    <!--  Menu Bar to navigate the app -->
    <MenuBar @toggle-modal="changeModal"/>

    <!--  Modal to display when a feature is not implemented yet -->
    <NotImplemented @toggle-modal="changeModal" :isActive="isActive" />
  </div>
</template>

<script>
import axios from "axios";
import { userStore } from "@/stores/userStore";
import { challengeStore } from "@/stores/challengeStore";

import MenuBar from "./MenuBar.vue";
import NotImplemented from "./NotImplemented.vue";

export default {
  name: "ChallengePage",
  components: {
    MenuBar,
    NotImplemented,
  },
  setup() {
    const user_store = userStore();
    const challenge_store = challengeStore();

    return {
      user_store,
      challenge_store,
    };
  },
  mounted() {
    this.getChallenges(this.challenge_store, this.user_store);
  },
  data() {
    return {
      isActive: false,
      challenges: [],
    };
  },
  methods: {
    changeModal() {
      // change the value of isActive
      this.isActive = !this.isActive;
    },
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
    getChallenges(challenge_store, user_store) {
      // Get 3 challenges from the backend, each challenge should be an object {id, title, fact, droplets}

      // check if there are challenges in the store before asking backend
      if (challenge_store.challenges.length > 0) {
        this.challenges = challenge_store.challenges;
      } else {
        axios
          .post("http://localhost:5000/api/challenges", {
              userId: user_store.userId, // the get request sends the id of the user to personalize the challenges sent
          })
          .then((response) => {
            console.log(response);
            if (response.data.status === "success") {
              this.challenges = response.data.challenges;
              challenge_store.challenges = response.data.challenges;
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style scoped>
#challenges-container {
  background-image: url("../assets/set_1/login_background.png");
  min-height: 100vh;
  background-repeat: repeat-y;
}
#challenges-title {
  color: rgb(6, 98, 132);
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  top: -50px;
}
.challenge {
  color: rgb(12, 50, 110);
  background-color: #ffffff;
  border-radius: 35px;
}
</style>
