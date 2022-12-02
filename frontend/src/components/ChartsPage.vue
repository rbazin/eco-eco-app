<template>
  <div id="charts-container" class="container">
      <!-- Back button -->
      <div @click="goBack" class="px-5 py-5 mb-5">
        <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left"/>
      </div>

      <!-- Progress title -->
      <h1 id="title" class="title is-1 has-text-centered">Progress</h1>

      <!-- weekly and monthly buttons-->
      <div class="button-container is-centered is-mobile">
        <div class="butt">
          <button @click="showWeeklyGraph" class="button is-primary is-light">Weekly</button>
        </div>
        <div class="butt" >
          <button @click="showMonthlyGraph" class="button is-primary is-light">Monthly</button>
        </div>
      </div>

      <!-- graphs -->
      <figure class="has-text-centered">
        <img v-bind:src="'data:image/jpeg;base64,'+monthlyGraph" v-if="showMonthly"/>
      </figure>
      <figure class="has-text-centered">
        <img v-bind:src="'data:image/jpeg;base64,'+weeklyGraph" v-if="showWeekly"/>
      </figure>

      <!--  Menu Bar to navigate the app -->
      <MenuBar/>

  </div>
</template>

<script>
import MenuBar from "./MenuBar.vue";
import axios from "axios";
import { userStore } from "@/stores/userStore";

export default {
  name: "ChartsPage",
  components: {
    MenuBar,
  },
  
  setup() {
    const store = userStore();
    return {
      store,
    };
  },

  data() {
    return {
    showWeekly: true,
    showMonthly: false,
    weeklyGraph:"",
    monthlyGraph:"",
    }
    
  },

  created() {
    axios 
      .post("http://localhost:5000/api/stats", {userId: this.store.userId,})
      .then((response) => {
        if (response.data.success) {
            this.weeklyGraph=response.data.weekly;
            this.monthlyGraph=response.data.monthly;
            this.showWeekly = true; //display weekly as default graph on page load
            this.showMonthly = false;
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },

  mounted() {
    this.showWeeklyGraph();
    this.showMonthlyGraph();
  },

  methods: {
    goBack() {
      this.$router.push("/home");
    },

    showMonthlyGraph() {
      this.showMonthly = true;
      this.showWeekly = false;
    },

    showWeeklyGraph() {
      this.showMonthly = false;
      this.showWeekly = true;
    },
  },
}
</script>

<style scoped>
#charts-container {
  background-image: url("../assets/set_1/login_background.png");
  background-repeat: repeat-y;
  min-height: 100vh;
}

.title {
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  top: -50px;
  color: #066284;
}
.button-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.butt {
  margin: 10px;
}
</style>
