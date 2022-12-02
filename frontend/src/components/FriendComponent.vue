<template>
  <div class="friend has-text-centered px-4 py-5 is-justify-content-center">
    <div class="columns is-mobile is-centered is-vcentered">
            <span class="column icon is-size-1"
            ><font-awesome-icon
                id="profile"
                color="darkviolet"
                icon="fa-solid fa-user fa-5x"
            /></span>
      <div class="column">
        <p class="is-size-4 username">{{ friend.FriendName }}</p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "FriendComponent",
  props: {
    friend: {
      type: Object,
      required: true,
    },
  },
}
</script>
<style scoped>
.friend {
  background: rgba(32, 196, 211, 0.27);
  border-radius: 35px;
  max-width: 300px;
  width: 80%;
  margin: 0 auto;
}
.username {
  color: #066284;
  font-weight: bold;
}
.column {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
</style>