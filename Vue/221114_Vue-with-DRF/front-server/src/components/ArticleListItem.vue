<template>
  <div>
    <router-link 
      :to="{
        name:'DetailView',
        params: { id : article.id }
      }"
    >
      [DETAIL]
    </router-link>
    <h5>{{article.id}}</h5>
    <p>{{article.title}}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article : Object
  }
}
</script>

<style>

</style>