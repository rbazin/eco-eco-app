<template>
  <div id="container-add-friend" class="container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left"/>
    </div>

    <!-- Main title -->
    <h1 id="title" class="title is-1 has-text-centered" >Add a friend</h1>

    <!-- Input field for adding a friend -->
    <div id="add-friend-button" class="field has-addons has-text-centered mx-5">
      <div class="control is-expanded">
        <input class="input is-large" :class="{'is-danger' : !isSuccess}" type="text" placeholder="Enter a username" v-model="username">
      </div>
      <div class="control">
        <a class="button is-large is-info" @click="addFriend">
          Add
        </a>
      </div>
    </div>
    <p id="help-text" class="subtitle is-4 has-text-centered has-text-danger" v-if="!isSuccess">Username not found</p>

    <figure id="friends-image" class="image has-text-centered">
      <img class="is-image" src="../assets/set_3/friends.png" />
    </figure>

    <!--  Menu Bar to navigate the app -->
    <MenuBar @toggle-modal="changeModal"/>

    <!--  Modal to display when a feature is not implemented yet -->
    <NotImplemented @toggle-modal="changeModal" :isActive="isActive"/>

  </div>
</template>
<script>
import MenuBar from "./MenuBar.vue";
import NotImplemented from "./NotImplemented.vue";

import { userStore } from "@/stores/userStore";

import axios from "axios";

export default {
  name: "AddFriendPage",
  components : {
    MenuBar,
    NotImplemented,
  },
  setup () {
    const store = userStore();
    return {
      store,
    };
  },
  data () {
    return {
      isActive : false,
      username: "",
      isSuccess: true,
    }
  },
  methods: {
    goBack() {
      this.$router.push("/friends");
    },
    changeModal() {
      this.isActive = !this.isActive;
    },
    addFriend() {
      // send a request to the backend to add a friend
      axios.post("http://localhost:5000/friend/add", {
        username: this.username,
      })
      .then((response) => {
        console.log(response);
        if (response.data.success) {
          this.store.userFriendList.push(response.data.friend); // assuming the backend returns the friend object
          this.$router.push("/friends");
        }
        else {
          this.isSuccess = false;
        }
      })
      .catch((error) => {
        console.log(error);
      });
      }
  }
}
</script>
<style scoped>
#container-add-friend {
  min-height: 100vh;
  background-image: url("../assets/set_1/login_background.png");
  background-repeat: repeat-y;
}
#title {
  color: rgb(6, 98, 132);
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  top: -50px;
}
#add-friend-button {
  position: relative;
  left: 50%;
  max-width: 500px;
  transform: translateX(-50%);
  min-width: 300px;
 width: 75%;
}
#friends-image {
  position: relative;
  width: 75%;
  left: 50%;
  transform: translateX(-50%);
  top: 100px;
}

</style>