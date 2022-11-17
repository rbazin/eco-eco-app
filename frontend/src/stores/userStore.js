import { defineStore } from "pinia";

export const userStore = defineStore("userStore", {
  state: () => ({
    userName: "",
    userId: null,
    userDroplets: 0,
    userStreak: 0,
    userTreeState: "",
    userFriendList: [],
    userActiveChallenge: null, // This may become an object with name and eco fact
    userLoggedIn: false,
    userMeansOfTransport: [],
  }),
  getters: {
    getUserData() {
      return {
        userName: this.userName,
        userId: this.userId,
        userDroplets: this.userDroplets,
        userStreak: this.userStreak,
        userTreeState: this.userTreeState,
        userFriendList: this.userFriendList,
        userActiveChallenge: this.userActiveChallenge,
        userLoggedIn: this.userLoggedIn,
      };
    },
  },
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
      this.userTreeState = "";
      this.userLoggedIn = false;
    },
  },
});
