import { defineStore } from "pinia";

export const challengeStore = defineStore("challengeStore", {
  state: () => ({
    challenges: [
      {
        id: 1,
        title: "Challenge 1",
        fact: "lorem ipsum",
      },
      {
        id: 2,
        title: "Challenge 2",
        fact: "lorem ipsum",
      },
      {
        id: 3,
        title: "Challenge 3",
        fact: "lorem ipsum",
      },
    ],
  }),
  getters: {
    getChallenges() {
      return this.challenges;
    },
  },
  actions: {
    async setChallenges(challenges) {
      this.challenges = challenges;
    },
  },
});
