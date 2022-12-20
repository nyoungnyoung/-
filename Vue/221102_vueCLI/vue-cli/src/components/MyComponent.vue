<template>
  <div>
    <h1>This is my component</h1>
    <MyItem static-props="component에서 child로" :dynamic-props="dynamicProps"/>
  </div>
</template>
<script>
import MyItem from '@/components/MyComponentItem.vue'
export default {
    name : 'MyComponent',
    components : {
        MyItem
    },
    data : function () {
      return {
        dynamicProps : "it's in data"
      }
    }
}
</script>

<style>

</style>