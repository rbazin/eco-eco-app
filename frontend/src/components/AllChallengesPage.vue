<template>
  <div id="container-all-challenges" class="container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left"/>
    </div>

    <h1 id="title-all-challenges" class="title has-text-centered is-1">All challenges</h1>

    <!-- Challenges -->
    <div
        v-for="(challenge, index) in challenges"
        :key="index"
        class="content mx-5 mb-5 py-5 challenge"
        @click="goToChallenge(challenge)"
    >
      <p class="is-size-4 px-5 has-text-centered">{{ challenge.title }}</p>
    </div>

    <!-- MenuBar to navigate the app -->
    <MenuBar @toggle-modal="changeModal"/>

    <!--  Modal to display when a feature is not implemented yet -->
    <NotImplemented @toggle-modal="changeModal" :isActive="isActive"/>

  </div>
</template>
<script>
import MenuBar from "./MenuBar.vue";
import NotImplemented from "./NotImplemented.vue";

import {userStore} from "@/stores/userStore";

import axios from "axios";

export default {
  name: "AllChallenges",
  components: {
    MenuBar,
    NotImplemented,
  },
  setup() {
    const user_store = userStore();
    return {
      user_store,
    };
  },
  mounted() {
    this.getAllChallenges();
  },
  data() {
    return {
      isActive: false,
      challenges: [],
    };
  },
  methods: {
    getAllChallenges() {
      axios
          .post("http://localhost:5000/api/challenge/all",
              {
                  userId : this.user_store.userId,
              }
          )
          .then((response) => {
            if (response.data.success) {
              this.challenges = response.data.challenges;
            }
          })
          .catch((error) => {
            console.log(error);
          });
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
      this.$router.push("/challenge");
    },
    changeModal() {
      // change the value of isActive
      this.isActive = !this.isActive;
    },
  },
};
</script>
<style scoped>
#container-all-challenges {
  position: relative;
  background-image: url("../assets/set_1/login_background.png");
  min-height: 100vh;
  background-repeat: repeat-y;
}

#title-all-challenges {
  position: relative;
  top: -50px;
  left: 50%;
  transform: translateX(-50%);
  color: rgb(6, 98, 132);
}
.challenge {
  color: rgb(12, 50, 110);
  background-color: #ffffff;
  border-radius: 35px;
}
</style>
