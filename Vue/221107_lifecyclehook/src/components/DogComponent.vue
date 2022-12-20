<template>
  <div>
    <button @click="getDogImage">멍멍아 이리온</button><br><br>
    <img v-if="imgSrc" :src="imgSrc" alt="#"><br>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name:'DogComponent',
  data() {
    return {
      imgSrc: null,
    }
  },
  methods:{
    getDogImage() {
      const dogImageSearchURL = 'https://dog.ceo/api/breeds/image/random'
      
      axios({
        method: 'get',
        url: dogImageSearchURL
      })
        .then((response) => {
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  // created 시점에서는 DOM 조작 할 수 없당..! 주석 처리된 코드 쓰면 error뜸
  created() {
    this.getDogImage()
    console.log('Child created!')
    // const btn = document.querySelector('button')
    // btn.innerText = '멍멍!'
  },
  // mounted 시점은 DOM조작 가능! created에서는 이게 안된다!
  mounted() {
    const btn = document.querySelector('button')
    btn.innerText = '멍멍!'
    console.log('Child mounted!')
  },
  // DOM에 수정사항이 있을 시점!
  updated() {
    console.log('새로운 멍멍!')
    console.log('Child updated!')
  }
}
</script>

<style>

</style>
