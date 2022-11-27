<template>
<div :class="{ 'disabled' : !badge.Possessed }" class="badge has-text-centered px-4 py-5 is-justify-content-center">
    <div class="columns is-mobile is-vcentered">
            <span class="column icon is-size-2"
            ><font-awesome-icon
                id="medal"
                color="rgb(32, 196, 211)"
                icon="fa-solid fa-medal fa-5x"
            /></span>
      <div class="column is-two-thirds">
        <p class="is-size-5 badge-name">{{ badge.BadgeName }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BadgeComponent",
  props: {
    badge: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped>
.badge {
  background: white;
  border-radius: 50px;
  max-width: 300px;
  width: 80%;
  margin: 0 auto;
}
.disabled {
  background-color: rgba(6, 6, 6, 0.2);
}
.disabled p {
  color: rgba(4, 4, 4, 0.2);
}
.disabled #medal {
  color: rgba(7, 7, 7, 0.2);
}
.badge-name {
  color: #066284;
}
.column {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
</style>