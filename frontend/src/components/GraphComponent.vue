<template>
  <div class="graphs">
    
    <!-- weekly and monthly buttons-->
      <div class="weekly">
        <button @click="showWeeklyGrpah" class="button is-primary is-light">Weekly</button>
      </div>
      <div class="monthly" >
        <button @click="showMonthlyGraph" class="button is-primary is-light">Monthly</button>
      </div>
    
    <slot :curGraph="curGraph"/>
      
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  setup() {
    //initialize with weekly
    const curGraph = ref(1);

    const showWeeklyGrpah = () => {
      if (curGraph.value === 1) {
        curGraph.value = 1;
        return;
      }
        else (curGraph.value === 2); {
        curGraph.value = 1;
      }
    }

    const showMonthlyGraph = () => {
      if (curGraph.value === 1) {
        curGraph.value = 2;
        return;
      }
      else (curGraph.value === 2); {
        curGraph.value = 2;
      }
    }

    return { curGraph, showWeeklyGrpah, showMonthlyGraph };
  },
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