<template>
  <div id="charts-container" class="container">
    <div class="ChartsPage">
      <!-- Back button -->
      <div @click="goBack" class="px-5 py-5">
        <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left"/>
      </div>

      <!-- Progress title -->
      <header>
        <p id="title" class="has-text-centered">Progress</p>
      </header>
  
      <!-- weekly and monthly buttons-->
      <div class="weekly">
        <button @click="showWeeklyGraph" class="button is-primary is-light">Weekly</button>
      </div>
      <div class="monthly" >
        <button @click="showMonthlyGraph" class="button is-primary is-light">Monthly</button>
      </div>

      <!-- graphs -->
      <img v-bind:src="'data:image/jpeg;base64,'+monthlyGraph" v-if="showMonthly"/>
      <img v-bind:src="'data:image/jpeg;base64,'+weeklyGraph" v-if="showWeekly"/>
    
      <!--  Menu Bar to navigate the app -->
      <MenuBar/>

    </div>
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

  mounted() {
    this.showWeeklyGraph();
    this.showMonthlyGraph();
  },

  methods: {
    goBack() {
      this.$router.push("/home");
    },

    showWeeklyGraph() {
      axios
        .post("http://localhost:5000/api/stats", {userId: this.store.userId,})
        .then((response) => {
          console.log(response.data.weekly);
          if (response.data.success) {
              this.weeklyGraph=response.data.weekly;
              this.showMonthly = false;
              this.showWeekly = true;
          }
        })
        .catch((error) => {
          console.log(error);
        });

    },

    showMonthlyGraph() {
      axios
        .post("http://localhost:5000/api/stats", {userId: this.store.userId,})
        .then((response) => {
          console.log(response);
          if (response.data.success) {
            this.monthlyGraph=response.data.monthly;
            this.showMonthly = true;
            this.showWeekly = false;
          }
        })
        .catch((error) => {
          console.log(error);
        });
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

.weekly {
  padding-top: 2rem;
  padding-left: 6rem;
  padding-bottom: 3rem;
  display: inline-block;
  --fa-border-color: rgb(10, 41, 99);
}

.monthly {
  padding-top: 2rem;
  padding-left: 1rem;
  padding-bottom: 3rem;
  display: inline-block;
  --fa-border-color: rgb(10, 41, 99);
}

</style>
