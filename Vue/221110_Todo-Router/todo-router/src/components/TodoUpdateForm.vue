<template>
  <div>
    <button @click="update">수정하기</button>
    <br>
    <input type="text" v-model="content">
    <br>
    <input type="date" v-model="date">
  </div>
</template>

<script>
export default {
    name: 'TodoUpdateForm',
    props: {
        todo: Object,
    },
    data() {
        return {
            nowtodo : this.todo,
            content : this.todo.content,
            date : this.todo.dueDateTime.slice(0,10)
        }
    },
    methods: {
        update() {
            this.nowtodo.content = this.content
            this.nowtodo.dueDateTime = this.date
            this.$store.dispatch('update', this.nowtodo)
            alert('수정완')
        }
    }
}
</script>

<style>

</style>