<template>
  <div>
    <h1>중요 할일</h1>
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
    name: 'ImportantTodoPage',
    components: {
      TodoListItem,
      TodoForm
    },
    computed: {
        todos() {
            const importTodos = this.$store.getters.allTodos.filter((todo) =>{
            return todo.isImportant === true
          })
          return importTodos
        }
    },
}
</script>

<style>

</style>