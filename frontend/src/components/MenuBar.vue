<template>
  <div id="menu-bar" class="container has-radius is-danger px-5 mx-5">
    <div class="columns is-mobile is-vcentered">
      <div @click="openModal" to="/friends" class="column">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/friends_white.png"
          alt="Friends icon"
        />
      </div>
      <div @click="openModal" to="/badges" class="column">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/badge.png"
          alt="Badge icon"
        />
      </div>
      <router-link to="/home" class="column">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/home_white.png"
          alt="Home icon"
        />
      </router-link>
      <div @click="openModal" class="column">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/graph_white.png"
          alt="Chart icon"
        />
      </div>
      <div @click="openModal" class="column">
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
.container {
  border-radius: 35px;
  background-color: rgba(32, 196, 211, 0.45);
}
</style>
