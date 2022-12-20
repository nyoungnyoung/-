<template>
  <input
    type="text"
    placeholder="할 일을 작성해주세요!"
    v-model.trim="todoTitle"
    @keyup.enter="createTodo">
</template>

<script>
export default {
    name: 'TodoForm',
    data() {
        return {
            todoTitle: null,
        }
    },
    methods: {
        createTodo() {
            if (this.todoTitle) {
                this.$store.dispatch('createTodo', this.todoTitle)
            }
            // 입력된 값 초기화해주기
            this.todoTitle = null
        }
    }
}
</script>

<style>

</style>