<template>
  <div class="mb-5">
    <div class="card bg-dark">
      <div>
        <div class="card-body">
          <form class="mb-4">
            <textarea
              class="form-control"
              rows="3"
              v-model.trim="comment"
              @keyup.enter="createComment"
              placeholder="댓글을 작성해주세요.  "
            ></textarea>
          </form>
          <toggle-button @change="isSpoiler()" />
          <div v-if="!spoiler" class="text-light">
            스포일러가 담긴 댓글을 작성하려면 클릭하세요!
          </div>
        </div>
      </div>
    </div>
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
      this.spoiler = !this.spoiler;
      return this.spoiler;
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
          spoiler: this.spoiler,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.$emit("create-comment", res);
        })
        .catch((err) => {
          console.log(err);
        });
      this.comment = null;
    },
  },
};
</script>

<style scoped>
.card {
  width: 56%;
  margin: 0 auto;
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.125);
  border-radius: 0.25rem;
}
.card-body {
  flex: 1 1 auto;
  padding: 1rem 1rem;
  /* display:block; */
  /* width:56%; */
  /* margin: 0 auto;  */
}
.form-control {
  display: block;
  /* width: 56%; */
  margin: 0 auto;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  background-color: #ced4da;
  background-clip: padding-box;
  border: 1px solid #ced4da;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
</style>
