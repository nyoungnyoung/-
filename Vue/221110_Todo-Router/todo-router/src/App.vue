<template>
  <div id="app">
    <b-container class="bv-example-row">
      <b-row class="text-center">
        <b-col>
          <SideBar/>
        </b-col>
          <!-- <nav>
            <router-link to="/">Home</router-link> |
            <router-link to="/about">About</router-link>
          </nav> -->
        <b-col cols="9">
          <router-view id="view"/>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import SideBar from '@/components/SideBar.vue'

export default {
  name: 'App',
  components: {
    SideBar
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
}

nav {
  padding: 30px;
  border: 4px solid #2c3e50;
  border-radius: 10px;
}

nav a {
  font-size: 4em;
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #42b983;
}

#view {
  padding: 30px;
  border: 4px solid #2c3e50;
  border-radius: 10px;
}
</style>
