import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [],
  },
  getters: {
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
    CHANGE_IMPORTANT(state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          todo.isImportant = !todo.isImportant
        }
        return todo
      })
    },
    UPDATE(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos[index] = todoItem
    },
  },
  actions: {
    // TodoForm.vue에서 input에 입력한 데이터 받아와서 todoItem 만들어준 뒤에 mutations 호출!
    createTodo(context, todoTitle) {
      const now = new Date()
      const todoItem = {
        id : now.getTime(),
        title: todoTitle,
        dueDateTime: `${now.getFullYear()}-${('0' + now.getMonth()).slice(-2)+1}-${('0' + now.getDate()).slice(-2)+1}T00:00`,
        isCompleted: false,
        isImportant: false,
      }
      // console.log(todoItem) -> todoItem 내용이 console에 찍힘
      context.commit('CREATE_TODO', todoItem)
    },
    // TodoListItem에서 호출되면 데이터 전달하면서 mutations 호출
    updateTodoStatus(context, todoItem) {
      context.commit('UPDATE_TODO_STATUS', todoItem)
    },
    changeImportant(context, todoItem) {
      context.commit('CHANGE_IMPORTANT', todoItem)
    },
    update(context, todoItem) {
      context.commit('UPDATE', todoItem)
    },
  },
  modules: {
  },
})
