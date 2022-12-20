<template>
  <div id="app">
    <h1>SSAFY TUBE</h1>
    <b-button variant="primary">Button</b-button>
    <SearchBar/>
    <VideoDetail/>
    <VideoList/>
  </div>
</template>

<script>
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'
import SearchBar from '@/components/SearchBar'

export default {
  name: 'App',
  components: {
    VideoList,
    VideoDetail,
    SearchBar,
  }
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
