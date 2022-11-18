<template>
  <div class="container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
    </div>

    <!-- Challenge info -->
    <div class="content has-text-centered">
      <h1 class="is-1 title pb-5">{{ challenge.title }}</h1>
      <div class="is-size-2">
        <span class="icon-text">
          <span class="icon"
            ><font-awesome-icon
              color="rgb(93, 173, 236)"
              icon="fa-solid fa-droplet"
          /></span>
          <span class="is-size-2">{{ challenge.droplets }}</span>
        </span>
      </div>
      <h2 class="subtitle is-3">DID YOU KNOW ?</h2>
      <p class="fact is-size-3">{{ challenge.fact }}</p>
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
  data() {
    return {
      challenge: {
        title: "",
        id: this.$route.params.id,
        fact: "",
        droplets: 0,
      },
    };
  },
  mounted() {
    this.challenge = this.challenge_store.challenges.find(
      (challenge) => challenge.id == this.$route.params.id
    );
  },
  methods: {
    goBack() {
      this.$router.push("/challenge"); // For the moment it will change the three challenges from the previous page
    },
    acceptChallenge() {
      // send the challenge to the backend
      axios
        .post("http://localhost:5000/api/accept_challenge", {
          userId: this.user_store.userId,
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
.fact {
  color: #055c52;
}
.title {
  color: #066284;
  text-shadow: 4 2 #1199ee;
}
.subtitle {
  color: #22aa99;
}
</style>
