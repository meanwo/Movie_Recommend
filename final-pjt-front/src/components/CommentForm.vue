<template>
  <div>
    <input type="text" v-model.trim="comment" @keyup.enter="createComment" />
    <toggle-button @change="isSpoiler()"/>
    <div v-if="!spoiler" class="text-light"> 스포일러가 담긴 댓글을 작성하려면 클릭하세요! </div>
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
      spoiler: false,
    };
  },
  methods: {
    isSpoiler() {
      this.spoiler = !this.spoiler
      return this.spoiler
    },
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
          spoiler: this.spoiler
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.$emit('create-comment', res)
          // this.$emit('spoiler', this.spoiler)
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

<style>

</style>