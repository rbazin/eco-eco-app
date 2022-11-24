<template>
  <div class="container main-container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
    </div>

    <!-- Content -->
    <div id="friends-container">
      <!-- Page title -->
      <h1 class="title is-1 has-text-centered">Friends</h1>

      <!-- Friends -->
      <FriendComponent class="mb-5" v-for="(friend, index) in friends" :key="index" :friend="friend" />

      <!--  Menu Bar to navigate the app -->
      <MenuBar @toggle-modal="changeModal"/>

    </div>
    <!--  Modal to display when a feature is not implemented yet -->
    <NotImplemented @toggle-modal="changeModal" :isActive="isActive"/>
  </div>
</template>
<script>
import FriendComponent  from "./FriendComponent.vue"
import MenuBar from "./MenuBar.vue"
import NotImplemented from "./NotImplemented.vue";

import { userStore } from "@/stores/userStore";

import axios from "axios";

export default {
  name: "App",
  components : {
    FriendComponent,
    MenuBar,
    NotImplemented,
  },
  setup() {
    const store = userStore();
    return {
      store,
    };
  },
  mounted() {
    this.getFriends();
  },
  data() {
    return {
      friends: [],
      isActive : false,
    }
  },
  methods: {
    changeModal() {
      // change the value of isActive
      this.isActive = !this.isActive;
    },
    goBack() {
      this.$router.push("/home");
    },
    getFriends() {
      if (this.store.userFriendList.length > 0) {
        this.friends = this.store.userFriendList;
        console.log(this.friends);
      }
      else {
        // TODO : check if the API call is compatible with the backend
        axios
            .get("http://localhost:5000/api/friends", {
              params: {
                user_id: this.store.user_id,
              },
            })
            .then((response) => {
              console.log(response);
              if (response.data.success) {
                this.friends = response.data.friends;
                this.store.userFriendList = response.data.friends;
              }
            })
            .catch((error) => {
              console.log(error);
            });
      }
    },
  }
};
</script>
<style scoped>
.title {
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  top: -50px;
  color: #066284;
}
.main-container {
  min-height: 100vh;
  background-image: url("../assets/set_1/login_background.png");
  background-repeat: repeat-y;
}

</style>
