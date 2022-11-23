<template>
  <div>
    <div v-if="comment.spoiler">
      주의! 스포일러가 담긴 댓글입니다!
      <toggle-button @change="showComment()" />
      <div v-if="checkSpoiler">
        <p>작성자 {{ comment.username }}</p>
        <p>댓글 {{ comment.content }}</p>
      </div>
    </div>
    <div v-else>
      <p>작성자 {{ comment.username }}</p>
      <p>댓글 {{ comment.content }}</p>
    </div>
    <button @click="deleteComment">X</button>
    <br />
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommentListItem",
  data() {
    return {
      checkSpoiler: false,

    };
  },
  props: {
    comment: Object,
  },
  methods: {
    deleteComment() {
      axios({
        method: "delete",
        url: `${API_URL}/api/v2/comments/${this.comment.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          
          this.$emit('delete-comment', this.comment.id)
          // this.$emit('delete-comment', res.data)
        })
        .catch((err) => {
          console.log(err)
        })

    },
    showComment() {
      this.checkSpoiler = !this.checkSpoiler;
      return this.checkSpoiler;
    },
  },
};
</script>

<style></style>
