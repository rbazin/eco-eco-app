<template>
  <div class="menu-bar container has-radius px-5">
    <div class="icons-container">
      <router-link to="/friends" class="px-1">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/friends_white.png"
          alt="Home icon"
        />
      </router-link>
      <div @click="openModal" class="px-1">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/badge.png"
          alt="Badge icon"
        />
      </div>
      <router-link to="/home" class="px-1">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/home_white.png"
          alt="Home icon"
        />
      </router-link>
      <div @click="openModal" class="px-1">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/graph_white.png"
          alt="Chart icon"
        />
      </div>
      <div @click="openModal" class="px-1">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/help.png"
          alt="Help icon"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MenuBar",
  // make a method to emmit isActive when an icon is clicked
  methods: {
    openModal() {
      this.$emit("toggleModal");
    },
  },
};
</script>

<style scoped>
.menu-bar {
  border-radius: 35px;
  background-color: rgba(32, 196, 211, 0.45);
  max-width: 400px;
  width: 90%;
  position: absolute;
  bottom: 1%;
  left: 50%;
  transform: translateX(-50%);
  min-height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.icons-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

</style>
