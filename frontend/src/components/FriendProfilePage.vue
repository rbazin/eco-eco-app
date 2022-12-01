<template>
  <div id="container-friend-profile" class="container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left"/>
    </div>

    <h1 id="main-title" class="title is-1 has-text-centered">{{ friendName }}</h1>

    <!-- Friend profile -->
    <div class="is-size-2 is-centered columns is-mobile">
      <figure class="column image">
        <img id="profile-pic" src="../assets/set_2/profile_pic_friend.png" alt="icon of user">
      </figure>
      <div class="column">
        <div class="columns ">
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

    <!-- Friend's Tree -->
    <figure class="has-text-centered image">
      <img id="tree-pic" :src="treePath" alt="tree of the user">
    </figure>

    <!-- Friend's Badges -->
    <h1 id="badge-title" class="title is-1 px-5">Badges</h1>
    <BadgeComponent v-for="(badge, index) in friendBadges" :badge="badge" :key="index" class="mt-5"/>

    <!--  Menu Bar to navigate the app -->
    <MenuBar/>

  </div>
</template>

<script>
import MenuBar from "./MenuBar.vue";
import BadgeComponent from "@/components/BadgeComponent.vue";

import axios from "axios";
import {userStore} from "@/stores/userStore";

export default {
  name: "FriendProfilePage",
  components: {
    MenuBar,
    BadgeComponent,
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
      friendName: "",
      friendDroplets: 0,
      friendStreak: 0,
      friendBadges: [],
    }
  },
  computed: {
    treePath() {
      return require("../assets/set_2/tree_" + this.getTreeState() + ".png");
    }
  },
  methods: {
    getTreeState() {
      if (this.friendDroplets < 600) {
        return Math.floor(this.friendDroplets / 100) + 1;
      }
      return 7;
    },
    getFriend() {
      axios
          .post("http://localhost:5000/api/friend", {
            FriendId: this.friendId,
            UserId: this.store.userId,
          })
          .then((response) => {
            if (response.data.success) {
              this.friendName = response.data.FriendName;
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
#main-title {
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  top: -50px;
  color: #066284;
}

#badge-title {
  color: #066284;
}

#profile-pic {
  width: 75%;
  max-width: 250px;
  height: auto;
}

#tree-pic {
  max-width: 250px;
  margin: auto;
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