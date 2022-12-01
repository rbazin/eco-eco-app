<template>
  <div id="container-friend-profile" class="container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left"/>
    </div>

    <h1 class="title is-1 has-text-centered">{{ friendName }}</h1>

    <!-- Friend profile -->
    <div class="is-size-2 is-centered columns py-6 is-mobile">
      <div class="column">
        <span class="icon"
        ><font-awesome-icon icon="fa-solid fa-circle-user fa-10x"
        /></span>
      </div>
      <div class="column">
        <div class="columns is-mobile">
          <div class="column">
        <span class="icon-text">
          <span class="icon"
          ><font-awesome-icon color="rgb(93, 173, 236)" icon="fa-solid fa-droplet"
          /></span>
          <span class="is-size-4">{{ friendDroplets }}</span>
        </span>
          </div>
          <div class="column">
        <span class="icon-text">
          <span class="icon"
          ><font-awesome-icon
              color="rgb(255, 172, 50)"
              icon="fa-solid fa-bolt-lightning fa-7x"
          /></span>
          <span class="is-size-4">{{ friendStreak }}</span>
        </span>
          </div>
        </div>
      </div>
    </div>

    <!--  Menu Bar to navigate the app -->
    <MenuBar/>

  </div>
</template>

<script>
import MenuBar from "./MenuBar.vue";

import axios from "axios";
import {userStore} from "@/stores/userStore";

export default {
  name: "FriendProfilePage",
  components: {
    MenuBar,
  },
  setup() {
    const store = userStore();
    return {
      store,
    };
  },
  mounted() {
    this.getFriend();
  },
  data() {
    return {
      friendId: this.$route.params.id,
      friendName: "Léonie",
      friendTreeState: 2,
      friendDroplets: 15,
      friendStreak: 5,
      friendBadges: [],
    }
  },
  methods: {
    getFriend() {
      axios
          .post("http://localhost:5000/api/friend", {
            FriendId: this.friendId,
            UserId: this.store.userId,
          })
          .then((response) => {
            if (response.data.success) {
              this.friendName = response.data.FriendName;
              this.friendTreeState = response.data.TreeState;
              this.friendDroplets = response.data.Droplets;
              this.friendStreak = response.data.Streak;
              this.friendBadges = response.data.Badges;
            }
          })
          .catch(error => {
            console.log(error);
          });
    },
    goBack() {
      this.$router.push("/friends");
    },
  }
}
</script>

<style scoped>
.title {
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  top: -50px;
  color: #066284;
}

.column {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

#container-friend-profile {
  min-height: 100vh;
  background-image: url("../assets/set_1/login_background.png");
  background-repeat: repeat-y;
}
</style>