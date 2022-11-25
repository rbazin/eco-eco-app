<template>
  <div class="container">
    <div class="ChartsPage">
      <!-- Back button -->
      <div @click="goBack" class="px-5 py-5">
        <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
      </div>

      <!-- Tutorial title -->
      <header>
        <p align="center">Progress</p>
      </header>


    </div>
  </div>
</template>

<script>
// import { userStore } from "@/stores/userStore";
// import axios from "axios";

export default {
  methods: {
      goBack() {
        this.$router.push("/home");
      },
    },
}
</script>

<style>
.container  {
  background-image: url("../assets/set_1/login_background.png");
  /* display: flex; */
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.ChartsPage {
  max-height: 100px;
}

p {
  font-size: 3rem;
  /* padding: 0rem; */
  text-align: center;
}

</style>
