<template>
  <div class="home">
    <h1>모든 할일</h1>
    <TodoForm/>
    <hr>
    <TodoList/>
    
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'AllTodoPage',
  components: {
    TodoForm,
    TodoList,
  }
}
</script>
