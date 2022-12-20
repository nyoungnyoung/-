<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home'}">홈으로!</router-link>
    <button @click="toHome">홈으로!</button>
    <br>
    <input
      type="text"
      v-model="inputData"
      @keyup.enter="toHello">
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    toHome() {
      this.$router.push({ name: 'home' })
    },
    toHello() {
      this.$router.push({ name: 'hello' , params: { userName: this.inputData }})
    },
  }
}
</script>