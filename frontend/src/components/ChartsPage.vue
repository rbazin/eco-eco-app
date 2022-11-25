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

      <!-- <div class="buttons">
        <button @click="showWeeklyGrpah" class="button is-primary is-light">Weekly</button>
        <button @click="showMonthlyGraph" class="button is-primary is-light">Monthly</button>
      </div> -->
      
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
import graphs from "../components/graphs.vue";

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

.buttons {
  justify-content: center;
  padding-top: 2rem;
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
