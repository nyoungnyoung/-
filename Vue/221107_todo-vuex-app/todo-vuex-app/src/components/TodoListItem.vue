<template>
    <div>
        <span @click="updateTodoStatus" :class="{'is-completed' : todo.isCompleted}">{{ todo.title }}</span>
        <button @click="deleteTodo">Delete</button>
    </div>
</template>

<script>
export default {
    name: 'TodoListItem',
    // 데이터 내려받을 때는 반드시 여기에 props 옵션 넣어줘야 함!
    props: {
        todo: Object,
    },
    methods: {
        deleteTodo() {
            // console.log('Todo 삭제')
            this.$store.dispatch('deleteTodo', this.todo)
        },
        updateTodoStatus() {
            this.$store.dispatch('updateTodoStatus', this.todo)
        }
    }
}
</script>

<style>
    .is-completed {
        text-decoration: line-through;
    }
</style>