<template>
  <div>
    <button @click="[btnClickEvent1(), btnClickVuex1()]">O</button>
    <button @click="[btnClickEvent0(), btnClickVuex0()]">X</button>
  </div>
</template>

<script>
export default {
  name: "BtnComponent",
  methods: {
    btnClickEvent0: function () {
      this.$emit("btn-click-event", "X");
    },
    btnClickEvent1: function () {
      this.$emit("btn-click-event", "O");
    },
    btnClickVuex0() {
      this.$store.dispatch("changeMessage", "X");
    },
    btnClickVuex1() {
      this.$store.dispatch("changeMessage", "O");
    },
  },
};
</script>

<style>
button {
  width: 80px;
  height: 45px;
  font-size: larger;
  background-color: coral;
  color: white;
  border: none;
  border-radius: 10px;
  margin: 10px;
  margin-bottom: -5px;
  font-weight: bolder;
}
</style>