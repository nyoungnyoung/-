import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store'
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
    doubleLength(state, getter) {
      return getters.messageLength * 2
    }
  },
  mutations: {
    // 얘는 왜 이름을 대문자로 했을까? 밑에 액션에 있는애랑 똑같이 해도 되지만,
    // mutations는 가장 중요한 역할을 해 주는 애이기 때문에 mutations라는걸 강조해주기 위해서!
    CHANGE_MESSAGE(state, newMessage) {
      console.log(state)
      console.log(newMessage)
    }
  },
  actions: {
    chnageMessage(context, newMessage) {
      // console.log(context)
      // console.log(newMessage)
      context.commit('mutation 메서드 이름', newMessage)
    }
  },
  modules: {
  }
})
