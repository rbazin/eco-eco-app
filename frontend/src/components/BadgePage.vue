<template>
  <div class="container" id="badges-container">
    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
    </div>
    <h1 id="badges-title" class="title is-1 has-text-centered">Badges</h1>

    <!-- Badges -->
    <BadgeComponent v-for="(badge, index) in badges" :key="index" :badge="badge" class="mt-5" />

    <!--  Menu Bar to navigate the app -->
    <MenuBar @toggle-modal="changeModal"/>

    <!--  Modal to display when a feature is not implemented yet -->
    <NotImplemented @toggle-modal="changeModal" :isActive="isActive" />
  </div>
</template>
<script>
import MenuBar from "@/components/MenuBar";
import NotImplemented from "@/components/NotImplemented";
import BadgeComponent from "@/components/BadgeComponent";

import { userStore } from "@/stores/userStore";

import axios from "axios";

export default {
  name: "BadgePage",
  components: {
    MenuBar,
    NotImplemented,
    BadgeComponent,
  },
  setup() {
    const user_store = userStore();
    return {
      user_store,
    };
  },
  mounted() {
    this.getBadges();
  },
  data() {
    return {
      isActive: false,
      badges: [],
    };
  },
  methods: {
    getBadges() {
      if (this.user_store.userBadges.length > 0) {
        // sort badges by possessed
        this.badges = this.user_store.userBadges.sort((a, b) => {
          return b.Possessed - a.Possessed;
        });
      }
      else {
        axios
          .post("http://localhost:5000/api/badges", {
              userId: this.user_store.userId,
          })
          .then((response) => {
            if (response.data.success) {
              this.badges = response.data.badges;
            }
          })
          .catch((error) => {
            console.log(error);
          });

      }
    },
    changeModal() {
      this.isActive = !this.isActive;
    },
    goBack() {
      this.$router.push('/home');
    },
  },
};
</script>
<style scoped>
#badges-container {
  background-image: url("../assets/set_1/login_background.png");
  min-height: 100vh;
  background-repeat: repeat-y;
}
#badges-title {
  color: rgb(6, 98, 132);
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  top: -50px;
}
</style>
