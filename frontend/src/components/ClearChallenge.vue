<template>
  <div class="modal" :class="{ 'is-active': isActive }">
    <div class="modal-background" @click="closeModal"></div>
    <div
      id="modal-content"
      class="modal-content has-background-white has-text-centered px-5 py-5"
    >
      <div id="button-container has-text-centered">
        <button @click="markComplete" class="button is-primary is-size-4 mb-5">
          Mark complete
        </button>
        <button @click="sendAbort" class="button is-danger is-size-4">
          Abort
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import { userStore } from "../stores/userStore";

export default {
  name: "Modal",
  setup() {
    const store = userStore();
    return {
      store,
    };
  },
  methods: {
    closeModal() {
      this.$emit("toggleModal");
    },
    completionReward(nbrDroplets, newStreak) {
      this.$emit("completionReward", nbrDroplets, newStreak);
    },
    markComplete() {
      // send request to backend to mark challenge as complete and update streak in store
      axios
        .post("/api/challenge/complete", {
          // Can I even access the store value like that ? What's the point of getters then ?
          challengeName: this.store.userActiveChallenge,
          challengeCompleted: true, // the backend should mark active challenge as null
          username: this.store.userName,
          userId: this.store.userId,
        })
        .then((response) => {
          if (response.status === "success") {
            this.store.userActiveChallenge = null;
            this.completionReward(
              response.data.userDroplets,
              response.data.userStreak
            ); // backend should return the droplets earned from completing the challenge and his new streak
            this.closeModal();
          }
          this.closeModal();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    sendAbort() {
      // send request to backend to mark challenge as aborted and update streak in store
      axios
        .post("/api/challenge/abort", {
          // Can I even access the store value like that ? What's the point of getters then ?
          challengeName: this.store.userActiveChallenge,
          challengeAborted: true, // the backend should mark active challenge as null
          username: this.store.userName,
          userId: this.store.userId,
        })
        .then((response) => {
          if (response.status === "success") {
            this.store.userActiveChallenge = null;
            this.closeModal();
          }
          this.closeModal();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  props: {
    isActive: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style scoped>
.modal-content {
  border-radius: 25px;
}
.button {
  width: 75%;
}
#button-container {
  display: flex;
  flex-direction: column;
}
</style>
