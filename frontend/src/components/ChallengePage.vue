<template>
  <div>
    <div class="challenge-page-challenge-page">
      <img
        alt="loginBackground"
        src="../assets/set_1/login_background.png"
        class="challenge-page-loginbackground1"
      />
      <img
        alt="Rectangle1"
        src="../assets/set_1/seeMoreRec.png"
        class="challenge-page-rectangle4"
      />
      <img
        alt="Rectangle2"
        src="../assets/set_1/rectangle.png"
        class="challenge-page-rectangle2"
      />
      <span class="challenge-page-text"><span>Take the metro to work</span></span>
      <span class="challenge-page-text02"><span>Challenges</span></span>
      <img
        alt="Arrow"
        src="../assets/set_1/arrow129-9gr2.svg"
        class="challenge-page-arrow1"
      />
      <img
        alt="Rectangle3"
        src="../assets/set_1/rectangle.png"
        class="challenge-page-rectangle1"
      />
      <img
        alt="Rectangle4"
        src="../assets/set_1/rectangle.png"
        class="challenge-page-rectangle3"
      />
      <span class="challenge-page-text04"><span>Go shopping by bike</span></span>
      <span class="challenge-page-text06">
        <span>
          <span>
            see
            <span v-html="rawiqif"></span>
          </span>
          <br />
          <span>more</span>
        </span>
      </span>
      <span class="challenge-page-text11"><span>Walk to school</span></span>
      <img
        alt="Arrow2220"
        src="/playground_assets/arrow2220-r5od.svg"
        class="challenge-page-arrow2"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChallengePage',
  props: {},

  data() {
    return {
      rawiqif: ' ',
    }
  },
}
</script>

<style scoped>
.challenge-page-challenge-page {
  width: 100%;
  height: 844px;
  display: flex;
  overflow: hidden;
  position: relative;
  align-items: flex-start;
  flex-shrink: 0;
  border-color: transparent;
  background-color: rgba(255, 255, 255, 1);
}
.challenge-page-loginbackground1 {
  top: -578px;
  left: -512px;
  width: 1414px;
  height: 2000px;
  position: absolute;
  border-color: transparent;
}
.challenge-page-rectangle4 {
  top: 624px;
  left: 243px;
  width: 128px;
  height: 60px;
  position: absolute;
  border-color: transparent;
  border-radius: 48px;
}
.challenge-page-rectangle2 {
  top: 467px;
  left: 61px;
  width: 269px;
  height: 128px;
  position: absolute;
  border-color: transparent;
  border-radius: 48px;
}
.challenge-page-text {
  top: 497px;
  left: 107px;
  color: rgba(12, 50, 110, 1);
  width: 194px;
  height: auto;
  position: absolute;
  font-size: 28px;
  align-self: auto;
  font-style: Regular;
  text-align: left;
  font-family: Roboto;
  font-weight: 400;
  line-height: normal;
  font-stretch: normal;
  margin-right: 0;
  margin-bottom: 0;
  text-decoration: none;
}
.challenge-page-text02 {
  top: 48px;
  left: 100px;
  color: rgba(6, 98, 132, 1);
  width: 251px;
  height: auto;
  position: absolute;
  font-size: 44px;
  align-self: auto;
  font-style: Medium;
  text-align: left;
  font-family: Montserrat;
  font-weight: 500;
  line-height: normal;
  font-stretch: normal;
  margin-right: 0;
  margin-bottom: 0;
  text-decoration: none;
}
.challenge-page-arrow1 {
  top: 35px;
  left: 67px;
  width: 51px;
  height: 0px;
  position: absolute;
}
.challenge-page-rectangle1 {
  top: 138px;
  left: 61px;
  width: 269px;
  height: 128px;
  position: absolute;
  border-color: transparent;
  border-radius: 48px;
}
.challenge-page-rectangle3 {
  top: 302px;
  left: 61px;
  width: 269px;
  height: 128px;
  position: absolute;
  border-color: transparent;
  border-radius: 48px;
}
.challenge-page-text04 {
  top: 339px;
  left: 112px;
  color: rgba(12, 50, 110, 1);
  width: 166px;
  height: auto;
  position: absolute;
  font-size: 28px;
  align-self: auto;
  font-style: Regular;
  text-align: left;
  font-family: Roboto;
  font-weight: 400;
  line-height: normal;
  font-stretch: normal;
  margin-right: 0;
  margin-bottom: 0;
  text-decoration: none;
}
.challenge-page-text06 {
  top: 627px;
  left: 259px;
  color: rgba(12, 50, 110, 1);
  width: 56px;
  height: auto;
  position: absolute;
  font-size: 23px;
  align-self: auto;
  font-style: Regular;
  text-align: left;
  font-family: Roboto;
  font-weight: 400;
  line-height: normal;
  font-stretch: normal;
  margin-right: 0;
  margin-bottom: 0;
  text-decoration: none;
}
.challenge-page-text11 {
  top: 182px;
  left: 100px;
  color: rgba(12, 50, 110, 1);
  width: 201px;
  height: auto;
  position: absolute;
  font-size: 28px;
  align-self: auto;
  font-style: Regular;
  text-align: left;
  font-family: Roboto;
  font-weight: 400;
  line-height: normal;
  font-stretch: normal;
  margin-right: 0;
  margin-bottom: 0;
  text-decoration: none;
}
.challenge-page-arrow2 {
  top: 655px;
  left: 322px;
  width: 31px;
  height: 0px;
  position: absolute;
}
@media(max-width: 479px) {
  .challenge-page-rectangle4 {
    top: 626px;
    right: 122px;
  }
  .challenge-page-rectangle1 {
    top: 132px;
    left: 59px;
  }
}
</style>
