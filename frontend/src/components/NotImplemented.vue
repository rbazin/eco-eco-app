<template>
  <div class="modal" :class="{ 'is-active': isActive }">
    <div class="modal-background"></div>
    <div class="modal-content has-background-white py-5 px-5 mx-0">
      <h1 class="title is-1">This feature has not been implemented yet !</h1>
    </div>
    <button
      @click="closeModal"
      class="modal-close is-large"
      aria-label="close"
    ></button>
  </div>
</template>

<script>
export default {
  name: "Modal",
  methods: {
    closeModal() {
      this.$emit("toggleModal");
    },
  },
  props: {
    isActive: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style></style>
