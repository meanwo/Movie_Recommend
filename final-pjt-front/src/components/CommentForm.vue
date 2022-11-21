<template>
  <div>
    <input type="text" v-model.trim="comment" @keyup.enter="createComment" />

    {{ movieCard.id }}
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommentForm",
  props: {
    movieCard: Object,
  },
  data() {
    return {
      comment: null,
    };
  },
  methods: {
    createComment() {
      const comment = this.comment;
      if (!comment) {
        alert("내용을 입력하세요!");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v2/movies/${this.movieCard.id}/comments/`,
        data: {
          content: comment,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.$emit('create-comment', res)
        })
        .catch((err) => {
          console.log(err);
        });
        this.comment = null    
    },
    // getComments() { 
    //     axios({
    //       method: 'get',
    //       url: `${API_URL}/api/v2/comments/list/${this.movieCard.id}/`
          
    //     })
    //       .then((res) => {
    //         // console.log(res)
    //         this.comments = res.data;
    //         console.log(this.comments)
    //       })
    //   },
  },
};
</script>

<style></style>
