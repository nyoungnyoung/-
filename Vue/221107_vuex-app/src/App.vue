<template>
  <div id="app">
    <!--<h1>{{ $store.state.message }}</h1>-->
    <h1>길이 {{ messageLengt }}의 메시지 {{ message }}를 입력받음</h1>
    <h3>X2 : {{ doubleLength }}</h3>
    <input type="text" @keyup.enter="chnageMessage" v-model="inputData">
    
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
    message() {
      return this.$store.state.message
    },
    messageLength() {
      return this.$store.getters.messageLengt
    },
    doubleLength() {
      return this.$store.getters.doubleLength
    }
  },
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
    }
  },
  computed
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
