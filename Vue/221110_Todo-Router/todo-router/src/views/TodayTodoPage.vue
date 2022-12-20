<template>
  <div>
    <h1>오늘 할일</h1>
    <TodoForm/>
    <hr>
    <TodoListItem
        v-for="todo in todos"
        :key="todo.id"
        :todo="todo"/>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
import TodoForm from '@/components/TodoForm'

export default {
    name: 'TodayTodoPage',
    components: {
      TodoListItem,
      TodoForm
    },
    computed: {
        todos() {
            const now = new Date()
            const year = now.getFullYear()
            const month = now.getMonth() + 1      // getMonth() : 1월이 0으로 표시됨
            const date = now.getDate()
            const today = `${year}-${month}-${date}`
            const todayTodos = this.$store.getters.allTodos.filter((todo) =>{
            return todo.dueDateTime === today
          })
          return todayTodos
        }
    },
}
</script>

<style>

</style>