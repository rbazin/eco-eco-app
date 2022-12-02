<template>
  <div id="help-container" class="container">

    <!-- Back button -->
    <div @click="goBack" class="px-5 py-5 mb-5">
      <font-awesome-icon class="is-size-2" icon="fa-solid fa-arrow-left"/>
    </div>

    <!-- Tutorial title -->
    <h1 id="title-help" class="title has-text-centered is-1">Help</h1>

    <!-- carousel -->
    <carousel align="center" class="carousel" v-slot="{currentSlide}">
      <slide v-for="(slide, index) in carouselSlides" :key="index">
        <!-- output the images -->
        <!-- show image only currentslide equals index -->
        <div v-show="currentSlide === index + 1" class="slide-content">
          <img class="help-img" :src="require(`../assets/helpImage/${slide}.png`)" alt=""/>
        </div>
      </slide>
    </carousel>

    <!--  Menu Bar to navigate the app -->
    <MenuBar/>

  </div>
</template>

<script>
import carousel from './CarouselComponent.vue';
import MenuBar from './MenuBar.vue';

export default {
  name: "HelpPage",
  components: {
    carousel,
    MenuBar,
  },
  setup() {
    const carouselSlides = ["h1", "h2", 'h3', 'h4', 'h5', 'h6', 'h7'];
    return {carouselSlides};
  },

  methods: {
    goBack() {
      this.$router.push("/home");
    },
  },
};
</script>

<style scoped>
.title {
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  top: -50px;
  color: #066284;
}

#help-container {
  background-image: url("../assets/set_1/login_background.png");
  background-repeat: repeat-y;
  /* display: flex; */
  align-items: center;
  justify-content: center;
  min-height: 100vh;

}


.carousel {
  padding-top: 10%;
  position: relative;
  max-height: 100vh;
  /* height: 88vh; */
  align-items: center;
}

.slide-content {
  position: relative;
  top: 0;
  left: 0;
  width: 100%;
  max-height: 100%;
  /* height: 100%; */
  vertical-align: middle;

}

.help-img {
  min-width: 50%;
  object-fit: contain;
  vertical-align: middle;
  max-width: 330px;
  max-height: 400px;
  width: auto;
  height: auto;
}
</style>
