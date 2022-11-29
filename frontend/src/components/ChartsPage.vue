<template>
  <div id="charts-container" class="container">
    <div class="ChartsPage">
      <!-- Back button -->
      <div @click="goBack" class="px-5 py-5">
        <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left"/>
      </div>

      <!-- Tutorial title -->
      <header>
        <p id="title" class="has-text-centered">Progress</p>
      </header>

      <graphs align="center" class="graphs" v-slot="{curGraph}">
        <slide v-for="(graph, index) in graphs" :key="index">
          <div v-show="curGraph === index + 1" class="the graph">
            <img id="graph" :src="require(`../assets/stats/${graph}.png`)" alt=""/>
          </div>
        </slide>
      </graphs>

      <!--  Menu Bar to navigate the app -->
      <MenuBar/>

    </div>
  </div>
</template>

<script>
import graphs from "./GraphComponent.vue";
import MenuBar from "./MenuBar.vue";

export default {
  name: "ChartsPage",
  components: {
    graphs,
    MenuBar,
  },
  setup() {
    const graphs = ["grah1", "graph2"];
    return {graphs};
  },
  methods: {
    goBack() {
      this.$router.push("/home");
    },
  },
}
</script>

<style scoped>
#charts-container {
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

#title {
  font-size: 3rem;
  /* padding: 0rem; */
  text-align: center;
}

#graph {
  min-width: 50%;
  object-fit: contain;
  vertical-align: middle;
  max-width: 400px;
  max-height: 400px;
  width: auto;
  height: auto;
}

</style>
