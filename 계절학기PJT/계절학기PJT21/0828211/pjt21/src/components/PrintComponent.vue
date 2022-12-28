<template>
  <div>
    <h1>props-emit 결과 : {{ yesNo }}</h1>
    <h1>vuex 결과 : {{ message }}</h1>
  </div>
</template>

<script>
export default {
  name: "PrintComponent",
  props: {
    yesNo: String,
  },
  computed: {
    message() {
      return this.$store.state.message;
    },
  },
};
</script>

<style>
</style>