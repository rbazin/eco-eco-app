<template>
  <div class="container has-radius is-danger px-5 mx-5">
    <div class="columns is-mobile is-vcentered">
      <router-link @click="openModal" to="/friends" class="column">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/friends_white.png"
          alt="Friends icon"
        />
      </router-link>
      <router-link @click="openModal" to="/badges" class="column">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/badge.png"
          alt="Badge icon"
        />
      </router-link>
      <router-link to="/home" class="column">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/home_white.png"
          alt="Home icon"
        />
      </router-link>
      <router-link @click="openModal" to="/charts" class="column">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/graph_white.png"
          alt="Chart icon"
        />
      </router-link>
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
      console.log("open modal");
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
