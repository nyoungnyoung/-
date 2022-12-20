<template>
  <div>
    <button @click="update">수정하기</button>
    <br>
    <input type="text" v-model="title">
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
            todoid : this.todo,
            title : this.todo.title,
            date : this.todo.dueDateTime.slice(0,10)
        }
    },
    methods: {
        update() {
            this.todoid.title = this.title
            this.todoid.dueDateTime = this.date
            this.$store.dispatch('update', this.todoid)
            
        }
    }
}
</script>

<style>

</style>