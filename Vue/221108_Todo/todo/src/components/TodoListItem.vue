<template>
    <div>
        <input type="checkbox" @click="updateTodoStatus" name="" id="">
        <span @click="clickTodo">{{ todo.title }}</span>
        <!-- changeimportant : v-if -->
        <span v-if="todo.isImportant" @click="changeImportant">💜</span>
        <span v-if="!todo.isImportant" @click="changeImportant">🤍</span>
        <!-- changeimportant : computed -->
        <span @click="changeImportant">{{ important }}</span>

        <TodoUpdateForm :todo="todo" v-show="isTodoClick"/>
    </div>
</template>

<script>
import TodoUpdateForm from '@/components/TodoUpdateForm'
export default {
    name:'TodoListItem',
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
            return this.todo.isImportant ? '💙' : '🤍'
        }
    },
    methods: {
        updateTodoStatus() {
            this.$store.dispatch('updateTodoStatus', this.todo)
        },
        changeImportant() {
            this.$store.dispatch('changeImportant', this.todo)
        },
        clickTodo() {
            this.isTodoClick = !this.isTodoClick
        },
    }
}
</script>

<style>

</style>