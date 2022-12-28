<template>
  <div id="app">
    <BtnComponent @btn-click-event="parentGetEvent" />
    <PrintComponent :yes-no="yesNo" />
  </div>
</template>

<script>
import BtnComponent from "./components/BtnComponent.vue";
import PrintComponent from "./components/PrintComponent.vue";

export default {
  name: "App",
  data() {
    return {
      yesNo: "",
    };
  },
  components: {
    BtnComponent,
    PrintComponent,
  },
  methods: {
    parentGetEvent: function (childData) {
      console.log(childData);
      this.yesNo = childData;
    },
  },
};
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
