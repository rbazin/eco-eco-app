import { defineStore } from "pinia";

export const userStore = defineStore("userStore", {
  state: () => ({
    userName: "",
    userId: null,
    userDroplets: 0,
    userStreak: 0,
    userTreeState: 1,
    userFriendList: [
      {
        userName: "Bob",
        userId: 1,
        userDroplets: 4,
        userStreak: 3,
      },
      {
        userName: "Clara",
        userId: 1,
        userDroplets: 4,
        userStreak: 3,
      }
    ],
    userActiveChallenge: null, // This may become an object with name and eco fact
    userLoggedIn: false,
    userMeansOfTransport: [],
    userFrequenciesOfTransport: [],
  }),
  actions: {
    async login(userId, userName, userDroplets, userStreak) {
      this.userName = userName;
      this.userId = userId;
      this.userDroplets = userDroplets;
      this.userStreak = userStreak;
      this.userLoggedIn = true;
    },
    async logout() {
      this.userName = "";
      this.userId = null;
      this.userDroplets = 0;
      this.userStreak = 0;
      this.userTreeState = 1;
      this.userLoggedIn = false;
    },
  },
});
