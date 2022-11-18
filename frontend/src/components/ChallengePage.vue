<template>
  <div class="container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ChallengePage",
  data() {
    return {
      challenges: {},
    };
  },
  methods: {
    goBack() {
      this.$router.push("/home");
    },
    // Function to get the challenge from the backend
    getChallenges() {
      // Get 3 challenges from the backend, each challenge should be an object {id, title, ecoFact}
      axios
        .get("http://localhost:5000/api/challenges")
        .then((response) => {
          console.log(response);
          if (response.data.success) {
            this.challenges = response.data.challenges;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped></style>
