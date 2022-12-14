<template>
  <div class="main-container pb-5">
    <!--  Header with droplets streaks and profile picture -->
    <div class="is-size-2 is-centered columns py-6 is-mobile">
      <div class="column is-narrow has-text-centered">
        <span class="icon-text">
          <span class="icon"
            ><font-awesome-icon color="rgb(93, 173, 236)" icon="fa-solid fa-droplet"
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
    <div id="main-content" class="mb-3">
      <div class="columns">
        <figure @click="clickOnCloud" id="cloud" class="column has-text-centered">
          <img :src="cloudPath" alt="cloud">
          <p id="cloud-text">{{ challengeText }}</p>
        </figure>
        <figure id="tree" class="column has-text-centered">
          <img :src="treePath" alt="tree of the user"/>
        </figure>
      </div>
    </div>

    <!--  Menu Bar to navigate the app -->
    <MenuBar @toggle-modal="changeModal"/>

    <!--  Modal to display when a feature is not implemented yet -->
    <NotImplemented @toggle-modal="changeModal" :isActive="isActive" />

    <!-- Modal to clear or abort the current challenge -->
    <ClearChallenge
      @abortion-effect="abortionEffect"
      @completion-reward="completionReward"
      @toggle-modal="changeModalClearChallenge"
      v-bind:isActive="clearChallengeModal"
    />
  </div>
</template>

<script>
// import MenuBar component
import MenuBar from "./MenuBar.vue";
import NotImplemented from "./NotImplemented.vue";
import ClearChallenge from "./ClearChallenge.vue";

import { userStore } from "../stores/userStore.js";

export default {
  name: "HomePage",
  components: {
    MenuBar,
    NotImplemented,
    ClearChallenge,
  },
  setup() {
    const store = userStore();
    return {
      store,
    };
  },
  data() {
    return {
      // We get most of the data from the userStore
      isActive: false,
      clearChallengeModal: false,
      droplets: this.store.userDroplets,
      streak: this.store.userStreak,
      profilePic: null,
      treeState: this.store.userTreeState, // 1 = grass, 2 = small tree, 3 = bigger tree, ...
      activeChallenge: this.store.userActiveChallenge,
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
      return require("../assets/set_2/tree_" + this.getTreeState() + ".png");
    },
  },
  methods: {
    getTreeState() {
      if (this.droplets < 600) {
        return Math.floor(this.droplets / 100) + 1;
      }
      return 7;
    },
    abortionEffect(newStreak) {
      this.streak = newStreak;
      this.activeChallenge = null;
    },
    completionReward(nbrDroplets, newStreak) {
      this.droplets = nbrDroplets;
      this.streak = newStreak;
      this.activeChallenge = null;
      this.store.userDroplets = nbrDroplets;
      this.store.userStreak = newStreak;
    },
    changeModal() {
      // change the value of isActive
      this.isActive = !this.isActive;
    },
    changeModalClearChallenge() {
      // change the value of clearChallengeModal
      this.clearChallengeModal = !this.clearChallengeModal;
    },
    clickOnCloud() {
      // Open the modal only if there is an active challenge
      if (this.activeChallenge) {
        this.changeModalClearChallenge();
      } else {
        // route to the challenges page
        this.$router.push("/challenge");
      }
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Sofia&display=swap");
.main-container {
  position: relative;
  background-image: url("../assets/set_1/login_background.png");
  min-height: 100vh;
  background-repeat: repeat-y;
  }
.columns {
  width: 100vw;
  margin: 0;
}
.column {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;  
}
img {
  width: 100%;
}
#cloud {
  position: relative;
}
#cloud img {
  max-width: 300px;
  margin: auto;
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
#tree img {
  max-width: 250px;
  margin: auto;
}
</style>
