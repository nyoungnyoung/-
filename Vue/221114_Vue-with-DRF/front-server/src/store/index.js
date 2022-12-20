import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    articles: [],
    token: null
  },
  getters: {
  },
  mutations: {
    // state에 정의되어있는 articles(현재는 빈 배열)에 actions에서 받아온 데이터(articles)를 넣어준다!
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // auth
    SIGN_UP(state, token) {
      state.token =token
    }
  },
  actions: {
    getArticles(context){
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/articles/`
      })
      .then((res)=>{
        // console.log(response, context)
        // console.log(res.data)
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
    
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then(res => {
        context.commit('SIGN_UP', res.data.key)
        })
        .catch(err => console.log(err))
    }
    },
  modules: {
  }
})