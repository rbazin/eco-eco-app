import { defineStore } from "pinia";

export const userStore = defineStore("userStore", {
  state: () => ({
    userName: "",
    userId: null,
    userDroplets: 0,
    userStreak: 0,
    userTreeState: "",
  }),
  getters: {
    getUserData() {
      return {
        userName: this.userName,
        userId: this.userId,
        userDroplets: this.userDroplets,
        userStreak: this.userStreak,
        userTreeState: this.userTreeState,
        userFriendList: [],
        userActiveChallenge: "",
      };
    },
  },
  actions: {
    async login(userId, userName, userDroplets, userStreak) {
      this.userName = userName;
      this.userId = userId;
      this.userDroplets = userDroplets;
      this.userStreak = userStreak;
    },
    async logout() {
      this.userName = "";
      this.userId = null;
      this.userDroplets = 0;
      this.userStreak = 0;
      this.userTreeState = "";
    },
  },
});
