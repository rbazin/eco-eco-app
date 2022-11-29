<template>
  <div class="container">
    <div class="ChartsPage">
      <!-- Back button -->
      <div @click="goBack" class="px-5 py-5">
        <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left" />
      </div>

      <!-- Tutorial title -->
      <header>
        <p class="has-text-centered">Progress</p>
      </header> 

      <graphs align="center" class="graphs" v-slot="{curGraph}">
          <slide v-for="(graph, index) in graphs" :key="index">
              <div v-show="curGraph === index + 1" class="the graph">
                  <img :src="require(`../assets/stats/${graph}.png`)" alt="" />
              </div>
          </slide>
      </graphs>

    </div>
  </div>
</template>

<script>
import graphs from "./GraphComponent.vue";

export default {
  name: "ChartsPage",
  components: {graphs},
  setup() {
      const graphs = ["grah1", "graph2"];
      return { graphs };
    },
  methods: {
      goBack() {
        this.$router.push("/home");
      },
  },
}
</script>

<style scoped>
.container  {
  background-image: url("../assets/set_1/login_background.png");
  background-repeat: repeat-y;
  /* display: flex; */
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

.ChartsPage {
  max-height: 100px;
}

p {
  font-size: 3rem;
  /* padding: 0rem; */
  text-align: center;
}

img {
  min-width: 50%;
  object-fit: contain;
  vertical-align: middle;
  max-width:400px;
  max-height:400px;
  width: auto;
  height: auto;
}

</style>
