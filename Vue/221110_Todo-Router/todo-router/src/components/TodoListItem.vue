<template>
  <div>
    <div class="mt-2 mb-2">
        <input @click="updateTodoStatus" type="checkbox"> 
        <span @click="clickTodo"> {{ todo.content }}</span>
        <span @click="changeImportant">{{ important }}</span>
    </div>
    <div>
        <TodoUpdateForm :todo="todo" v-show="isTodoClick"/>
    </div>
  </div>
</template>

<script>
import TodoUpdateForm from '@/components/TodoUpdateForm';

export default {
    name: 'TodoListItem',
    data() {
        return {
            isTodoClick:false,
        }
    },
    props: {
        todo: Object,
    },
    components: {
        TodoUpdateForm,
    },
    computed: {
        important() {
            return this.todo.isImportant? '💙' : '🤍'
        }
    },
    methods: {
        clickTodo() {
            this.isTodoClick = !this.isTodoClick
        },
        updateTodoStatus() {
            this.$store.dispatch('updateTodoStatus', this.todo)
        },
        changeImportant() {
            this.$store.dispatch('changeImportant', this.todo)
        }
    }
}
</script>

<style>

</style>