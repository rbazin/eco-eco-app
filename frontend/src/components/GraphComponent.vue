<template>
  <div class="graphs">
    
    <!-- weekly and monthly buttons-->
      <div class="weekly">
        <button @click="showWeeklyGrpah" class="button is-primary is-light">Weekly</button>
      </div>
      <div class="monthly" >
        <button @click="showMonthlyGraph" class="button is-primary is-light">Monthly</button>
      </div>
    
    <!-- <slot :curGraph="curGraph"/> -->

    <img src='weeklyGraph' v-if='showWeekly' />
    <img src='monthlyGraph' v-if="showMonthly" />
    
      
  </div>
</template>

<script>
// import { ref } from "vue";
import axios from "axios";
export default {
  data: {
    showWeekly: false,
    showMonthly: false,
  },

  mounted() {
    this.showWeeklyGrpah();
    this.showMonthlyGraph();
  },

  methods: {
    showWeeklyGrpah() {
      axios
        .get("http://localhost:5000/api/stats", {userId: this.store.userId,})
        .then((response) => {
          console.log(response);
          if (response.data.success) {
              console.log(response.data);
            this.showWeekly = !this.showWeekly;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    showMonthlyGrpah() {
      axios
        .get("http://localhost:5000/api/stats", {userId: this.store.userId,})
        .then((response) => {
          console.log(response);
          if (response.data.success) {
            
            console.log(response.data);
            this.showMonthly = !this.showMonthly;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  }
  // setup() {
  //   //initialize with weekly
  //   const curGraph = ref(1);

  //   const showWeeklyGrpah = () => {
  //     if (curGraph.value === 1) {
  //       curGraph.value = 1;
  //       return;
  //     }
  //       else (curGraph.value === 2); {
  //       curGraph.value = 1;
  //     }
  //   }

  //   const showMonthlyGraph = () => {
  //     if (curGraph.value === 1) {
  //       curGraph.value = 2;
  //       return;
  //     }
  //     else (curGraph.value === 2); {
  //       curGraph.value = 2;
  //     }
  //   }

  //   return { curGraph, showWeeklyGrpah, showMonthlyGraph };
  // },
};
</script>

<style scoped>
.weekly {
  padding-top: 2rem;
  padding-left: 1rem;
  padding-top: 0%;
  display: inline-block;
  --fa-border-color: rgb(10, 41, 99);
}

.monthly {
  padding-top: 2rem;
  padding-left: 3rem;
  display: inline-block;
  --fa-border-color: rgb(10, 41, 99);
}
</style>