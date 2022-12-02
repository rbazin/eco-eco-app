<template>
  <div class="container">
    <div class="TutorialPage">

      <!-- Tutorial title -->
    <header>
        <p align="center">Tutorial </p>
    </header>

      <!-- carousel -->
    <carousel align="center" class="carousel" v-slot="{currentSlide}"> 
        <slide v-for="(slide, index) in carouselSlides" :key="index">
            <!-- output the images -->
            <!-- show image only currentslide equals index -->
            <div v-show="currentSlide === index + 1" class="slide-content">
                <img :src="require(`../assets/helpImage/${slide}.png`)" alt="" />
            </div>
        </slide>
    </carousel>

    <!-- "I'm ready!"" button -->
    <div class="field px-6 py-6">
    <div class="control has-text-centered">
        <button @click="ready" class="button is-primary" >
        I'm ready!
        </button>
    </div>
    </div>
      
    </div>
  </div>
</template>

<script>
import carousel from './CarouselComponent.vue';
// import slide from '../components/slide.vue';

export default {
    name: "HelpPage",
    components: {carousel},
    setup() {
      const carouselSlides = ["h1", "h2",'h3','h4','h5','h6','h7'];
      return { carouselSlides };
    },

    methods: {
      ready() {
        this.$router.push("/home");
      },
    },
};
</script>

<style scoped>
.container  {
  background-image: url("../assets/set_1/login_background.png");
  /* display: flex; */
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.TutorialPage {
    max-height: 100px;
    /* height: 100%; */
}

p {
  font-size: 3rem;
  padding-top: 2rem;
  /* padding: 0rem; */
  text-align: center;
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
img {
  min-width: 50%;
  object-fit: contain;
  vertical-align: middle;
  max-width:330px;
  max-height:400px;
  width: auto;
  height: auto;
}

</style>
