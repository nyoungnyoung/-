<template>
  <div>
    <TodoListItem
        v-for="todo in todos"
        :key="todo.id"
        :todo="todo"/>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
    name: 'TodoList',
    components: {
        TodoListItem,
    },
    data() {
        return {
            todos: this.$store.getters.allTodos,
        }
    },
    // computed: {
    //     todos() {
    //         return this.$store.getters.allTodos.todos
    //     }
    // }
}
</script>

<style>

</style>