<template>
  <div class="main-container is-fullheight container">
    <!--  Header with droplets streaks and profile picture -->
    <div class="is-size-2 is-centered columns py-6 is-mobile has-text-centered">
      <div class="column is-narrow">
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
    <div class="main-content">
      <div class="columns is-centered is-hcentered has-text-centered">
        <figure class="column has-text-centered" width="75%">
          <img class="image" src="../assets/set_2/cloud.png" />
        </figure>
        <figure class="column has-text-centered">
          <img class="image" src="../assets/set_2/tree_1.png" />
        </figure>
      </div>
    </div>
    <!--  Menu Bar to navigate the app -->
    <MenuBar @toggle-modal="changeModal" />
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
      treeState: "",
      activeChallenge: null,
      pathTree: "../assets/set_2/tree_1.png",
    };
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

<style>
.main-container {
  background-image: url("../assets/set_1/login_background.png");
  height: 100vh;
}
</style>
