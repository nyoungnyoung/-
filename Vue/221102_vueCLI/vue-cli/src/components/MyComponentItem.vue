<template>
  <div>
    <h1>아이템</h1>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
  </div>
</template>

<script>
export default {
    name : 'MyItem',
    props : {
      staticProps: String,
      dynamicProps: String,
    }
}
</script>

<style>

</style>