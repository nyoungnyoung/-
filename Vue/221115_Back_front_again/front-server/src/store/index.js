import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [],
    token: null
  },
  getters: {
    // token이 있으면 true, 없으면 false 반환함!
    isLogin (state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // auth
    SIGN_UP(state, token){
      state.token = token
    },

    // sign up && login
    SAVE_TOKEN(state, token){
      state.token = token
      router.push({ name: 'ArticleView' })
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        // 요청 보낼 때 headers에 Token을 함께 보내주기 위해!
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then(res => {
          // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
          }
        )
        .catch(err => console.log(err))
    },

    // auth
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
          // context.commit('SIGN_UP', res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => console.log(err))
    },

    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => console.log(err))
    },
  },
  modules: {
  }
})
