<template>
  <div class="article-list">
    <h3>Article List</h3>
    <ArticleListItem
    v-for="article in articles"
    :article="article"
    :key="article.id"/>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem.vue'
export default {
  name: 'ArticleList',
  components: {
    ArticleListItem
  },
  computed: {
    articles(){
      return this.$store.state.articles
    }
    }
  }
</script>

<style>
.article-list {
  text-align: start;
}
</style>