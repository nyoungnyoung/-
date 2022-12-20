export default {
  state: {
    todos: [
      {
        id : new Date().getTime(),
        content : 'Module Test',
        dueDateTime : '2022-11-11',
        isCompleted : false,
        isImportant : true
      },
      {
        id: 1638771553377,                // nowDateObj.getTime()
        content: 'Vue',                   // Todo 내용
        dueDateTime: '2021-12-09',  // 마감일
        isCompleted: false,               // 완료된 할 일
        isImportant: true,                        // 중요 할 일
      },
      {
        id: 1638771553378,
        content: 'Vue Router',
        dueDateTime: '2021-12-10',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 16387715533779,
        content: 'Vuex',
        dueDateTime: '2021-12-11T00:00',
        isCompleted: true,
        isImportant: false,
      },
    ]
  },
  getters: {
    // 여기다가 getter 이름을 allTodos로 설정해놓았다면
    // this.$store.getter.allTodos.todo 이런식으로 가져올수 있다는 뜻인듯?
    allTodos(state){
      return state.todos
    },
    // importTodos(state){
    //   const importTodos = state.todos.filter((todo) =>{
    //     return todo.isImportant === true
    //   })
    // }
  },
  mutations: {
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
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    UPDATE(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos[index] = todoItem
    },
  },
  actions: {
    // TodoListItem에서 호출되면 데이터 전달하면서 mutations 호출
    updateTodoStatus(context, todo) {
      context.commit('UPDATE_TODO_STATUS', todo)
    },
    changeImportant(context, todo) {
      context.commit('CHANGE_IMPORTANT', todo)
    },
    // TodoForm.vue에서 input에 입력한 데이터 받아와서 todoItem 만들어준 뒤에 mutations 호출!
    createTodo(context, todoTitle) {
      const now = new Date()
      const year = now.getFullYear()
      const month = now.getMonth() + 1      // getMonth() : 1월이 0으로 표시됨
      const date = now.getDate()
      const todoItem = {
        id : now.getTime(),
        content: todoTitle,
        dueDateTime: `${year}-${month}-${date}`,
        isCompleted: false,
        isImportant: false,
      }
      // console.log(todoItem) -> todoItem 내용이 console에 찍힘
      context.commit('CREATE_TODO', todoItem)
    },
    update(context, todoItem) {
      context.commit('UPDATE', todoItem)
    },
  },
  modules: {
  }
}
