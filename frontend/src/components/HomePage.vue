<template>
  <div class="main-container">
    <!--  Header with droplets streaks and profile picture -->
    <div class="is-size-2 is-centered columns py-6 is-mobile">
      <div class="column is-narrow has-text-centered">
        <span class="icon-text">
          <span class="icon"
            ><font-awesome-icon
              color="rgb(93, 173, 236)"
              icon="fa-solid fa-droplet"
          /></span>
          <span class="is-size-4">{{ droplets }}</span>
        </span>
      </div>
      <div class="column is-narrow">
        <span class="icon-text">
          <span class="icon"
            ><font-awesome-icon
              color="rgb(255, 172, 50)"
              icon="fa-solid fa-bolt-lightning fa-7x"
          /></span>
          <span class="is-size-4">{{ streak }}</span>
        </span>
      </div>
      <div class="column is-narrow">
        <span class="icon"
          ><font-awesome-icon icon="fa-solid fa-circle-user fa-7x"
        /></span>
      </div>
    </div>

    <!--  Main content -->
    <div id="main-content" class="mb-6">
      <div class="columns">
        <figure id="cloud" class="column has-text-centered">
          <img :src="cloudPath" />
          <p id="cloud-text">{{ challengeText }}</p>
        </figure>
        <figure class="column has-text-centered">
          <img :src="treePath" />
        </figure>
      </div>
    </div>

    <!--  Menu Bar to navigate the app -->
    <MenuBar @toggle-modal="changeModal" id="menu-bar" />
    <NotImplemented @toggle-modal="changeModal" :isActive="isActive" />
  </div>
</template>

<script>
// import MenuBar component
import MenuBar from "./MenuBar.vue";
import NotImplemented from "./NotImplemented.vue";

import { userStore } from "../stores/userStore.js";

export default {
  name: "HomePage",
  components: {
    MenuBar,
    NotImplemented,
  },
  setup() {
    const store = userStore();
    return {
      store,
    };
  },
  data() {
    return {
      isActive: false,
      droplets: 0,
      streak: 0,
      profilePic: null,
      treeState: 1, // 1 = grass, 2 = small tree, 3 = bigger tree, ...
      activeChallenge: null,
    };
  },
  computed: {
    challengeText: function () {
      if (this.activeChallenge) {
        return "Challenge in progress";
      } else {
        return "Select a challenge";
      }
    },
    cloudPath: function () {
      if (this.activeChallenge) {
        return require("../assets/set_2/cloud_gray.png");
      } else {
        return require("../assets/set_2/cloud.png");
      }
    },
    treePath: function () {
      return require("../assets/set_2/tree_" + this.treeState + ".png");
    },
  },
  methods: {
    changeModal() {
      // change the value of isActive
      this.isActive = !this.isActive;
    },
    // get the user's data from store : should launch right from the beginning
    async getUserData() {
      const data = this.store.getUserData();
      this.droplets = data.userDroplets;
      this.streak = data.userStreak;
      // this.profilePic = data.userProfilePic; // We should fetch the profile pic but for now it will be static
      this.treeState = data.userTreeState;
      this.activeChallenge = data.userActiveChallenge;
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Sofia&display=swap");
.main-container {
  background-image: url("../assets/set_1/login_background.png");
  height: 100vh;
}
.columns {
  width: 100vw;
  margin: 0;
}
img {
  width: 75%;
  height: auto;
}
#cloud {
  position: relative;
}
#cloud-text {
  font-family: "Sofia", cursive;
  color: #3e7568;
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1.5rem;
  font-weight: bold;
}
</style>
