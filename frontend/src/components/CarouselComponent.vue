<template>
  <div class="carousel">
    <slot :currentSlide="currentSlide"/>
    <!-- navigation buttons-->
      <div class="navigateLeft" @click="prevSlide">
        <font-awesome-icon class="is-size-2" icon="fa-solid fa-chevron-left" border/>
      </div>
      <div class="navigateRight" @click="nextSlide" >
        <font-awesome-icon class="is-size-2" icon="fa-solid fa-chevron-right" border/>
      </div>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  setup() {
    // let the slide start with first img
    const currentSlide = ref(1);
    // const getSlideCount = ref(null);

    // next slide
    const nextSlide = () => {
      if (currentSlide.value === 7) {
        currentSlide.value = 7;
        return;
      }
      currentSlide.value += 1
    }

    //previous slide
    const prevSlide = () => {
      if (currentSlide.value === 1 ) {
        // currentSlide.value = getSlideCount.value;
        currentSlide.value = 1;
        return;
      }
      currentSlide.value -= 1;
    }
    // onMounted ( () => {
    //   getSlideCount.value = document.querySelectorAll(".slide").length;
    // });

    return { currentSlide, nextSlide, prevSlide };
  },
};
</script>

<style scoped>
.navigate {
  padding: 0 16px;
  width: 100%;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
}

.navigateLeft {
  padding-top: 2rem;
  padding-left: 1rem;
  padding-top: 0%;
  display: inline-block;
  --fa-border-color: rgb(10, 41, 99);
}

.navigateRight {
  padding-top: 2rem;
  padding-left: 3rem;
  display: inline-block;
  --fa-border-color: rgb(10, 41, 99);
}

</style>