import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: []
  },
  getters: {
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      // 1. 완료된 todo만 모아놓은 새로운 객체 생성
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted == true
      })
      // 2. 길이 반환
      return completedTodos.length
    },
    unCompletedTodosCount(state, getters) {
      return getters.allTodosCount - getters.completedTodosCount
    },
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem) {
      // console.log(todoItem)
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      // console.log(todoItem)
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
    // LOAD_TODOS(state) {
    //   const localStorageTodos = localStorage.getItem('todos')
    //   const parsedTodos = JSON.parse(localStorageTodos)
    //   state.todos = parsedTodos
    // },
  },
  actions: {
    createTodo(context, todoTitle) {
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      // console.log(todoItem) -> 확인용
      context.commit('CREATE_TODO', todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    updateTodoStatus(context, todoItem) {
      context.commit('UPDATE_TODO_STATUS', todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    // F12 - Application - Storage 다양한 저장소 중 local Storage에 저장해주기
    // saveTodosToLocalStorage(context) {
    //   const jsonTodos = JSON.stringify(context.state.todos)
    //   localStorage.setItem('todos', jsonTodos)
    // },
    // local Storage에서 데이터 불러오기
    // loadTodos(context) {
    //   context.commit('LOAD_TODOS')
    // }
  },
  modules: {
  },
  // vuex-persistedstate : Vuex state를 자동으로 브라우저의 Local Storage에 저장해주는 라이브러리
  plugins: [
    createPersistedState(),
  ],
})
