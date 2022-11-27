import {defineStore} from "pinia";

export const userStore = defineStore("userStore", {
    state: () => ({
        userName: "",
        userId: null,
        userDroplets: 0,
        userStreak: 0,
        userTreeState: 1,
        userFriendList: [
            {
                FriendName: "Bob",
                FriendId: 1,
                challenge: null,
            },
            {
                FriendName: "Clara",
                FriendId: 1,
                challenge: null,
            }
        ],
        userActiveChallenge: null, // This may become an object with name and eco fact
        userLoggedIn: false,
        userMeansOfTransport: [],
        userFrequenciesOfTransport: [],
        userBadges: [],
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
