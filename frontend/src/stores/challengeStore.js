import { defineStore } from "pinia";

export const challengeStore = defineStore("challengeStore", {
  state: () => ({
    challenges: [
      {
        id: 1,
        title: "Challenge 1",
        fact: "lorem ipsum",
        reward: 10,
      },
      {
        id: 2,
        title: "Challenge 2",
        fact: "lorem ipsum",
        reward: 20,
      },
      {
        id: 3,
        title: "Challenge 3",
        fact: "lorem ipsum",
        reward: 30,
      },
    ],
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
