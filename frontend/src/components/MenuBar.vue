<template>
  <div class="container has-radius is-danger px-5 mx-5">
    <div class="columns is-mobile is-vcentered">
      <router-link to="/friends" class="column">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/friends_white.png"
          alt="Friends icon"
        />
      </router-link>
      <router-link to="/badges" class="column">
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
      <router-link to="/charts" class="column">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/graph_white.png"
          alt="Chart icon"
        />
      </router-link>
      <router-link to="/guide" class="column">
        <img
          class="image is-48x60 content"
          src="../assets/set_2/help.png"
          alt="Help icon"
        />
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "MenuBar",
};
</script>

<style scoped>
.container {
  border-radius: 35px;
  background-color: rgba(32, 196, 211, 0.45);
}
</style>
