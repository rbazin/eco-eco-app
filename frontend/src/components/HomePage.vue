<template>
  <div class="main-container is-fullheight container">
    <div class="container v-centered columns">
      <div class="column">
        <span class="icon-text">
          <span class="icon"
            ><font-awesome-icon
              color="rgb(93, 173, 236)"
              icon="fa-solid fa-droplet"
          /></span>
          <span class="is-size-4">Home</span>
        </span>
      </div>
    </div>
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
      this.profilePic = data.userProfilePic; // We should fetch the profile pic but for now it will be static
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
