<template>
  <div class="article-list">
    <h3>Article List</h3>
    <ArticleListItem v-for="article in articles"
    :key="article.id"
    :article="article"/>
    <!-- : 이용해서 props로 article 넘겨주기! -->
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  computed: {
    // 이렇게해서 중앙 저장소에 저장되어있는 articles을 가져와서, 내가 갖고있도록 computed이용!
    articles() {
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