import { defineStore } from "pinia";

export const challengeStore = defineStore("challengeStore", {
  state: () => ({
    challenges: [],
    allChallenges: [],
  }),
  getters: {
    // get challenge by id
    getChallengeFromId: (state) => {
      return (challengeId) =>
        state.challenges.find((challenge) => challenge.id === challengeId);
    },
  },
  actions: {
    async setChallenges(challenges) {
      this.challenges = challenges;
    },
  },
});
