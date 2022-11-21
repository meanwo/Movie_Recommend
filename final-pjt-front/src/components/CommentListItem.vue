<template>
  <div>
    <p>작성자 {{comment.username}}</p>
    <p>댓글 {{comment.content}}</p>
    <br>
  </div>
</template>

<script>
export default {
    name: 'CommentListItem',
    props: {
        comment: Object,
    }
}
</script>

<style>

</style>